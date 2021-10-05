

import pandas as pd

class soccer():

    def __init__(self,filepath):
        self.df = pd.read_csv(filepath)
        origin_df  = self.df

    def high_win_perc(self):
        self.df['win_perc'] = (self.df['Wins'] / self.df['Games']) * 100
        self.df = self.df.sort_values(by=['win_perc'], ascending=False).reset_index(drop=True)
        self.df_top_10 = self.df[:10].copy(deep=True)
        self.list_top10_teams = self.df_top_10['Team'].tolist()
        return self.list_top10_teams

    def most_draws(self):
        self.df_most_draws = self.df.sort_values(by=['Draws'], ascending=False).copy(deep=True).reset_index(drop=True)
        self.df_most_draws_team = self.df_most_draws[:1].drop(columns=['win_perc'])
        return self.df_most_draws_team


    def stats_display(self):
        print ("*************************************Stats Display******************************")
        print("list_top10_teams", self.list_top10_teams)
        print("Team Stats having most draws : ", self.df_most_draws_team)
        self.df['goal_diff']= self.df['Goals'] - self.df['Goals Allowed']
        self.df['goal_diff_abs']=self.df['goal_diff'].abs()
        self.gols_min = self.df.loc[self.df['goal_diff_abs'].idxmin()]
        print ("team name :",self.gols_min['Team'])
        print ("***********************************Completed************************************")
        return self.gols_min['Team']




#filepath = 'C:\Users\Gathi\Documents\test\soccer.csv'
filepath = 'C:/Users/Gathi/Documents/test/soccer.csv'
df = pd.read_csv(filepath)
df1 = soccer(filepath)
print (df1.high_win_perc())
print (df1.most_draws())
print (df1.stats_display())







# class soccer():
#
#     def __init__(self,filepath):
#         self.filepath=filepath
#
#
# df = pd.read_csv(r'C:\Users\Anurag\Desktop\soccer.csv')
#
# df['win_perc'] = (df['Wins']/df['Games'])*100
#
# df = df.sort_values(by=['win_perc'],ascending=False).reset_index(drop=True)
#
# df_top_10 = df[:10].copy(deep=True)
#
# list_top10_teams = df_top_10['Team'].tolist()
#
# df_most_draws = df.sort_values(by=['Draws'],ascending=False).copy(deep=True).reset_index(drop=True)
#
# df_most_draws_team = df_most_draws[:1].drop(columns=['win_perc'])
#
# print("list_top10_teams", list_top10_teams)
# print("Team Stats having most draws \n", df_most_draws_team)
# df1['goal_diff']= df1['Goals'] - df1['Goals Allowed']
# df1['goal_diff_abs']=df1['goal_diff'].abs()
# df1.loc[df1['goal_diff_abs'].idxmin()]
