import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class HourlyPlot:
    # Automate preparing the datasets for concatenation
    def drop_timevalues(dataset):
        new_dataset = dataset.drop(axis = 1, columns = 'Time')
        new_dataset = new_dataset.reset_index()
        new_dataset = new_dataset.drop(axis = 1, columns = 'index')
        return new_dataset


    # A function to automate the splitting into hourly values
    # and plotting an overlapping plot to identify trend and occurences above/below threshold
    def hourly_plot(datapath):
        raw = pd.read_csv(datapath)
        #factor to help us split the dataset into hours, time dimension for values is 100ms
        f = 60 * 60 * 10

        #splitting the values
        hour0 = raw[:f]
        hour1 = raw[f:2*f]
        hour2 = raw[2*f:3*f]
        hour3 = raw[3*f:4*f]
        hour4 = raw[4*f:5*f]
        hour5 = raw[5*f:6*f]
        hour6 = raw[6*f:7*f]
        hour7 = raw[7*f:8*f]
        hour8 = raw[8*f:9*f]
        hour9 = raw[9*f:10*f]
        hour10 = raw[10*f:11*f]
        hour11 = raw[11*f:12*f]
        hour12 = raw[12*f:13*f]
        hour13 = raw[13*f:14*f]
        hour14 = raw[14*f:15*f]
        hour15 = raw[15*f:16*f]
        hour16 = raw[16*f:17*f]
        hour17 = raw[17*f:18*f]
        hour18 = raw[18*f:19*f]
        hour19 = raw[19*f:20*f]
        hour20 = raw[20*f:21*f]
        hour21 = raw[21*f:22*f]
        hour22 = raw[22*f:23*f]
        hour23 = raw[23*f:]

        # Creating a new dataframe with data organised in hourly columns
        hour0 = drop_timevalues(hour0)
        hour1 = drop_timevalues(hour1)
        hour2 = drop_timevalues(hour2)
        hour3 = drop_timevalues(hour3)
        hour4 = drop_timevalues(hour4)
        hour5 = drop_timevalues(hour5)
        hour6 = drop_timevalues(hour6)
        hour7 = drop_timevalues(hour7)
        hour8 = drop_timevalues(hour8)
        hour9 = drop_timevalues(hour9)
        hour10 = drop_timevalues(hour10)
        hour11 = drop_timevalues(hour11)
        hour12 = drop_timevalues(hour12)
        hour13 = drop_timevalues(hour13)
        hour14 = drop_timevalues(hour14)
        hour15 = drop_timevalues(hour15)
        hour16 = drop_timevalues(hour16)
        hour17 = drop_timevalues(hour17)
        hour18 = drop_timevalues(hour18)
        hour19 = drop_timevalues(hour19)
        hour20 = drop_timevalues(hour20)
        hour21 = drop_timevalues(hour21)
        hour22 = drop_timevalues(hour22)
        hour23 = drop_timevalues(hour23)

        hour0 = hour0.rename(columns = {'Value': 'Hour0'})
        hour1 = hour1.rename(columns = {'Value': 'Hour1'})
        hour2 = hour2.rename(columns = {'Value': 'Hour2'})
        hour3 = hour3.rename(columns = {'Value': 'Hour3'})
        hour4 = hour4.rename(columns = {'Value': 'Hour4'})
        hour5 = hour5.rename(columns = {'Value': 'Hour5'})
        hour6 = hour6.rename(columns = {'Value': 'Hour6'})
        hour7 = hour7.rename(columns = {'Value': 'Hour7'})
        hour8 = hour8.rename(columns = {'Value': 'Hour8'})
        hour9 = hour9.rename(columns = {'Value': 'Hour9'})
        hour10 = hour10.rename(columns = {'Value': 'Hour10'})
        hour11 = hour11.rename(columns = {'Value': 'Hour11'})
        hour12 = hour12.rename(columns = {'Value': 'Hour12'})
        hour13 = hour13.rename(columns = {'Value': 'Hour13'})
        hour14 = hour14.rename(columns = {'Value': 'Hour14'})
        hour15 = hour15.rename(columns = {'Value': 'Hour15'})
        hour16 = hour16.rename(columns = {'Value': 'Hour16'})
        hour17 = hour17.rename(columns = {'Value': 'Hour17'})
        hour18 = hour18.rename(columns = {'Value': 'Hour18'})
        hour19 = hour19.rename(columns = {'Value': 'Hour19'})
        hour20 = hour20.rename(columns = {'Value': 'Hour20'})
        hour21 = hour21.rename(columns = {'Value': 'Hour21'})
        hour22 = hour22.rename(columns = {'Value': 'Hour22'})
        hour23 = hour23.rename(columns = {'Value': 'Hour23'})

        daily = hour0
        daily = daily.join([hour1, hour2, hour3, hour4, hour5,
                            hour6, hour7, hour8, hour9, hour10,
                            hour11, hour12, hour13, hour14, hour15,
                            hour16, hour17, hour18, hour19, hour20,
                            hour21, hour22, hour23])

        # Finally, plot the values using SEABORN
        sns.set_theme(style = 'dark')
        g = sns.lineplot(data = daily,
                         linewidth = 0.25,
                         legend = False)
        g.axhline(50.1, linewidth = 1, linestyle = ':')
        g.axhline(49.9, linewidth = 1, linestyle = ':')

        # Saving the plot as png
        name = (((datapath.split('/'))[2]).split('.'))[0]
        plt.savefig(f'{name}.png', dpi = 300)
        return daily, g

if __name__ == "__main__":

    print("You meant to import this")