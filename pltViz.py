# Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class viz:

    def __init__(self,df,fig_title,size = (10,5)):
        '''
        init class
        '''
        self.df = df
        self.fig = plt.figure(figsize = size)
        self.fig.suptitle(fig_title)
    
    def fig_adjust(self,w,h):
        '''
        adjust the figure margins
        '''
        self.fig.subplots_adjust(wspace=w, hspace=h)

    def box(self,x,*args):
        '''
        box plot
        '''
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        ax.set_ylabel(x)
        ax.set_title("Boxplot of {}".format(x))
        ax.boxplot(self.df[x])

    def hist(self,x,*args):
        ''' 
        histgram
        '''
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        ax.set_ylabel(x)
        ax.set_title('Histogram of {}'.format(x))
        ax.hist(self.df[x], alpha=0.5)

    def scatter(self,x,y,lw,alpha,*args):
        '''
        scatter plot
        '''
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title('Scatterplot of {} and {}'.format(x,y))
        ax.scatter(self.df[x],self.df[y],alpha = alpha, linewidths = lw)

    def bar(self,x,*args):
        '''
        bar plot for categorical variables
        '''
        data = dict(self.df[x].value_counts())
        names = list(data.keys())
        values = list(data.values())
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        ax.set_xlabel('levels')
        ax.set_ylabel(x)
        ax.set_title('Barplot of {}'.format(x))
        ax.bar(names,values)

    def stackedBar(self,idx,col,*args):
        '''
        stacked bar plot
        idx and col must be categorical
        '''
        df = pd.crosstab(self.df[idx],self.df[col])
        df2 = pd.crosstab(self.df[idx],self.df[col],normalize='columns')
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        btm = [0 for i in range(len(df.columns))]
        for d in range(len(df.index)):
            y = df.iloc[d,:].values
            x = df.columns
            ax.bar(x,y,label = df.index[d],bottom = btm)
            btm += y
            for n in range(len(df.columns)):
                ax.text(n,btm[n],'{}  [{:.0%}]'.format(df.iloc[d,n],df2.iloc[d,n]),va = 'top',ha = 'center',size = 'small')
            hans, labs = ax.get_legend_handles_labels()
            ax.legend(handles = hans, labels = labs,title = df.columns.name)
            ax.set_xlabel('levels of {}'.format(df.index.name))
            ax.set_ylabel(df.columns.name)
            ax.set_title('Stacked barplot of {} and {}'.format(df.index.name,df.columns.name))

    def stackedBarPercent(self,idx,col,*args):
        '''
        stacked percent bar plot
        idx and col must be categorical
        '''
        df = pd.crosstab(self.df[idx],self.df[col],normalize='columns')
        ax = self.fig.add_subplot(args[0],args[1],args[2])
        btm = [0 for i in range(len(df.columns))]
        for d in range(len(df.index)):
            y = df.iloc[d,:].values
            x = df.columns
            ax.bar(x,y,label = df.index[d],bottom = btm)
            btm += y
            for n in range(len(df.columns)):
                ax.text(n,btm[n],'{:.0%}'.format(df.iloc[d,n]),va = 'top',ha = 'center',size = 'small')
            hans, labs = ax.get_legend_handles_labels()
            ax.legend(handles = hans, labels = labs,title = df.columns.name)
            ax.set_xlabel('levels of {}'.format(df.index.name))
            ax.set_ylabel(df.columns.name)
            ax.set_title('Stacked percent barplot of {} and {}'.format(df.index.name,df.columns.name))
            
    def show(self):
        '''
        get the figure
        '''
        return self.fig

    def save(self,dir):
        '''
        save the figure
        '''
        self.fig.savefig(dir)