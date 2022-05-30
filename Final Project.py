#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Create a file called 'Plots' in the home directory with the following structure 
# Plots 
# -> 'Name of your scan ex. Supreethi_1776 '
#   -> 'Single'
#   -> 'Both'
#   -> 'Off'
#   -> 'Shifted'


# In[19]:


import sys, os
sys.path.append(os.path.join(os.environ['HOME'], 'setiS22'))
sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Single')
sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Both')
sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Off')
sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Shifted')
#sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Techno_candidates/Single')
#sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Techno_candidates/Both')
#sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Techno_candidates/Off')
#sys.path.append('/data/seti/epss179S22/natsuko725/Plots/Techno_candidates/Shifted')


# In[20]:


from seti.globals import TIME_PER_ROW, OBSERVATIONS  # may take 5 seconds or more to execute - be patient!
from seti.globals.utilities import CONFIG
from seti.sql import get_data
import seti.figures.tfdiagram as tfd
from seti import CandidateSignal
import matplotlib.pyplot as plt


# In[21]:


OBSERVATIONS.info['NAME']


# In[22]:


Supreethi_1776 = OBSERVATIONS.info['NAME'].iloc[12] 
Supreethi_1776_techno = get_data(name=Supreethi_1776,  FAND='Y', scan=1)
Supreethi_1776_RFI = get_data(name=Supreethi_1776,  FDOP='Y', scan=1)
print('no. of technosignature candidates: ', len(Supreethi_1776_techno))
print('no. of RFI candidates: ', len(Supreethi_1776_RFI))


# In[6]:


Supreethi_1776_RFI_freq = Supreethi_1776_RFI[(Supreethi_1776_RFI['FREQ'] > 1.55*10**9) & (Supreethi_1776_RFI['FREQ'] < 1.6*10**9)]
print('no. of RFI candidates in my freq. range: ', len(Supreethi_1776_RFI_freq))


# In[24]:


# Technosignature Candidate Plots


# In[ ]:


techno_CandidateSignals = []
for i in range(len(Supreethi_1776_techno)):
    techno_CandidateSignals.append(CandidateSignal(Supreethi_1776_techno['ID'].iloc[i]))


# In[25]:


for i in range(len(techno_CandidateSignals)):
    techno_CandidateSignals[i].plot(dfdt = True, show = False, snr_thresh = 10)
    filename = str(techno_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Single/' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[8]:


for i in range(len(techno_CandidateSignals)):
    techno_CandidateSignals[i].bothscans(show = False)
    filename = str(techno_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Both/' + 'both_scans_' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[26]:


for i in range(len(techno_CandidateSignals)):
    techno_CandidateSignals[i].offscan(show = False, snr_thresh = 10)
    filename = str(techno_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Off/' + 'off_scan_' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[ ]:


for i in range(len(techno_CandidateSignals)):
    techno_CandidateSignals[i].shift_data()
    techno_CandidateSignals[i].plot(dfdt = True, show = False)
    filename = str(techno_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/Supreethi_1776/Shifted/' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[ ]:


# RFI Class Plots


# In[ ]:


RFI_CandidateSignals = []
for i in range(5000, 9000, 50):
    RFI_CandidateSignals.append(CandidateSignal(Supreethi_1776_RFI_freq['ID'].iloc[i]))


# In[ ]:


for i in range(len(RFI_CandidateSignals)):
    RFI_CandidateSignals[i].plot(dfdt = True, show = False)
    filename = str(RFI_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/RFI_candidates/Single/' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[ ]:


for i in range(len(RFI_CandidateSignals)):
    RFI_CandidateSignals[i].shift_data()
    RFI_CandidateSignals[i].plot(dfdt = True, show = False)
    filename = str(RFI_CandidateSignals[i].id)
    save_dir = '/data/seti/epss179S22/natsuko725/Plots/RFI_candidates/Shifted/' + filename + '.png'
    plt.savefig(save_dir)
    plt.close()


# In[9]:


RFI_list = [6517756, 6517810, 6517915, 6517968, 6518018, 6517706, 6519352, 6518018, 8664401, 8664351, 8664251, 8664053]


# In[60]:


n = 11
RFI = get_data(ID=RFI_list[n])
RFI_cand = CandidateSignal(RFI_list[n])
RFI


# In[61]:


RFI_cand.plot()


# In[62]:


RFI_cand.allscans()


# In[63]:


RFI_cand.bothscans()


# In[21]:


from seti.sql import get_data_with_clause


# In[72]:


df = 0 
lower_lim = (RFI_cand.freq * 10**6 + (df-300))
upper_lim = (RFI_cand.freq * 10**6 + (df+300))
get_data_with_clause("WHERE FREQ BETWEEN %s and %s", parameters=[lower_lim, upper_lim])


# In[32]:


tfd.plot(1333351, pvf=False, dfdt = True, snr_thresh = 10)


# In[18]:


tfd.offscan(2043000, snr_thresh = 10)


# In[28]:


tfd.allscans(1333608, snr_thresh = 10)


# In[88]:


from seti.figures.plot_RFI_class import plot_RFI_class
plot_RFI_class(signal_id = 8664053, other_signals = [6517756, 6517810, 6517915, 6517968, 6518018, 6517706, 6519352, 6518018, 8664401, 8664351, 8664251])

