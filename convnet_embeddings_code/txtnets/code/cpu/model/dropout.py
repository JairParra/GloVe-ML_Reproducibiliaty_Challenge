__author__ = 'albandemiraj, mdenil'

import numpy as np
import cpu.space
import cpu.model.layer
import generic.model.dropout
from cpu.model.model import CSM
from cpu.model.transfer import SentenceConvolution
from cpu.model.transfer import Softmax
from cpu.model.transfer import Linear


class Dropout(generic.model.dropout.Dropout, cpu.model.layer.Layer):
    def _get_mask(self, shape):
        mask = np.random.uniform(size=shape) < (1.0 - self.dropout_rate)
        mask_space = cpu.space.CPUSpace.infer(mask, self.axes)
        return mask, mask_space

    # bprop is generic
    # no grads

    def __repr__(self):
        return "{}(R={})".format(
            self.__class__.__name__,
            self.dropout_rate)


def _remove_dropout_softmax(smax, ratio):
    new_smax = Softmax(
        n_classes=smax.n_classes,
        n_input_dimensions=smax.n_input_dimensions)

    new_smax.W = smax.W.copy() * (1-ratio)
    new_smax.b = smax.b.copy()
    return new_smax


def _remove_dropout_linear(linear, ratio):
    new_linear = Linear(
        n_input=linear.n_input,
        n_output=linear.n_output)

    new_linear.W = linear.W.copy() * (1-ratio)
    return new_linear


def _sentence_convolution(conv_layer, ratio):
    new_conv = SentenceConvolution(
        n_feature_maps=conv_layer.n_feature_maps,
        kernel_width=conv_layer.kernel_width,
        n_channels=conv_layer.n_channels,
        n_input_dimensions=conv_layer.n_input_dimensions)

    new_conv.W = conv_layer.W.copy() * (1-ratio)
    return new_conv


def _identity(layer, ratio):
    return layer


__function_mapping = {
    'Softmax': _remove_dropout_softmax,
    'SentenceConvolution': _sentence_convolution,
    'Linear': _remove_dropout_linear,
    'Tanh': _identity,
    'Bias': _identity,
    'MaxFolding': _identity,
    'SumFolding': _identity,
    'WordEmbedding': _identity,
    'DictionaryEncoding': _identity
}


def remove_dropout(model):
    new_model = []
    ratio = 0
    for layer in model.layers:
        if layer.__class__.__name__ == 'Dropout':
            ratio = layer.dropout_rate
        else:
            if ratio == 0:
                new_model.append(layer)
            else:
                new_model.append(__function_mapping[layer.__class__.__name__](layer, ratio))
                ratio = 0

    return CSM(layers=new_model)
