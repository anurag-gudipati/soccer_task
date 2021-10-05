

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
        print ("team name with smallest difference in for and against goals :",self.gols_min['Team'])
        print ("***********************************Completed************************************")
        return self.gols_min['Team']





filepath = 'soccer.csv'
df = pd.read_csv(filepath)
df1 = soccer(filepath)
print (df1.high_win_perc())
print (df1.most_draws())
print (df1.stats_display())

