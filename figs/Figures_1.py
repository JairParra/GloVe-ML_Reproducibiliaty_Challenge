#!/usr/bin/env python
# coding: utf-8

# In[54]:


import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np


# In[55]:


# Data from demo.sh run using vector_size = 300, window_size = 15, iterations = 50, and x_max = 100

capital_common_countries = 86.76
capital_world = 47.19
currency = 11.07
city_in_state = 47.12
family = 49.05
gram1_adjective_to_adverb = 3.53
gram2_opposite = 4.23
gram3_comparative = 39.49
gram4_superlative = 9.58
gram5_present_participle = 9.19
gram6_nationality_adjective = 70.15
gram7_past_tense = 15.26
gram8_plural = 28.75
gram9_plural_verbs = 8.97

q_seen_v_total = 91.21

semantic_accuracy = 47.07
syntactic_accuracy = 24.50
total_accuracy = 33.89

running_time = '4 hours and 11 mins'

cost = [0.020423, 0.013536, 0.012321,0.011302,0.010410,0.009692,0.009098,0.008597,0.008161,0.007781,0.007450,0.007156,0.006894,0.006656,0.006441,0.006247,0.006072,0.005903,0.005747,0.005607,0.005478,0.005361,0.005251,0.005149,0.005054,0.004964,0.004881,0.004801,0.004729,0.004661,0.004598,0.004538,0.004482,0.004430,0.004333,0.004288,0.004244,0.004203,0.004162,0.004088,0.004054,0.004021,0.003989,0.003930,0.003904,0.003877,0.003852]

accuracies = [capital_common_countries, capital_world, currency, city_in_state, family, gram1_adjective_to_adverb, gram2_opposite,
             gram3_comparative, gram4_superlative, gram5_present_participle, gram6_nationality_adjective, gram7_past_tense,
             gram8_plural, gram9_plural_verbs]


# In[56]:


fig, ax = plt.subplots()
x = np.arange(14)
plt.bar(x, accuracies)
plt.xticks(x, ('Capital_Common_Countries', 'Capital_World', 'Currency', 'City_in_State', 'Family', 'gram1_adjective_to_adverb',
              'gram2_opposite','gram3_comparative','gram4_superlative','gram5_present_participle','gram6_nationality_adjective',
              'gram7_past_tense','gram8_plural','gram9_plural_verbs'))
plt.xticks(rotation=90)
labels = ['Capital_Common_Countries', 'Capital_World', 'Currency', 'City_in_State', 'Family', 'gram1_adjective_to_adverb',
              'gram2_opposite','gram3_comparative','gram4_superlative','gram5_present_participle','gram6_nationality_adjective',
              'gram7_past_tense','gram8_plural','gram9_plural_verbs']

ax.set_ylabel('Accuracy')
plt.show()


# In[57]:


plt.plot(cost)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Training Evolution of Cost')
plt.show()


# In[ ]:




