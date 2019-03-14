
# coding: utf-8

# In[1]:


from tqdm import tqdm_notebook


# In[2]:


class ReciprocalRank:
    
    def __init__(self, rc_list, query):
        self.rc_list = rc_list
        self.query = query
        
    def mrr(self):
        my_sum = 0
        for i, j in tqdm_notebook(zip(self.rc_list, self.query)):
            if j in i:
                recip_rank = 1 / (i.index(j) + 1)
            else:
                recip_rank = 0
            my_sum += recip_rank
        return my_sum / len(self.query)

