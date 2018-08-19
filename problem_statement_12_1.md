
# Problem Statement 12_1

# 1


```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
```


```python
df['FlightNumber']
```




    0    10045.0
    1        NaN
    2    10065.0
    3        NaN
    4    10085.0
    Name: FlightNumber, dtype: float64




```python
df['FlightNumber'][1] = 10055
df['FlightNumber'][3] = 10075
```

    c:\users\vinay raj manchala\appdata\local\programs\python\python35\lib\site-packages\ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.
    c:\users\vinay raj manchala\appdata\local\programs\python\python35\lib\site-packages\ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    


```python
df['FlightNumber'] = df['FlightNumber'].astype('int')
```


```python
df['FlightNumber'].dtype
```




    dtype('int32')



# 2


```python
df[['From','To']] = df['From_To'].str.split('_',expand=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>From_To</th>
      <th>RecentDelays</th>
      <th>From</th>
      <th>To</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>LoNDon_paris</td>
      <td>[23, 47]</td>
      <td>LoNDon</td>
      <td>paris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>MAdrid_miLAN</td>
      <td>[]</td>
      <td>MAdrid</td>
      <td>miLAN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>londON_StockhOlm</td>
      <td>[24, 43, 87]</td>
      <td>londON</td>
      <td>StockhOlm</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>Budapest_PaRis</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>PaRis</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>Brussels_londOn</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>londOn</td>
    </tr>
  </tbody>
</table>
</div>



# 3


```python
col_values = df['From'].values
converted_values = []

for col in col_values:
    converted_values.append(col.title())
df['From'] = converted_values

col_values = df['To'].values
converted_values = []

for col in col_values:
    converted_values.append(col.title())
df['To'] = converted_values
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>From_To</th>
      <th>RecentDelays</th>
      <th>From</th>
      <th>To</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>LoNDon_paris</td>
      <td>[23, 47]</td>
      <td>London</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>MAdrid_miLAN</td>
      <td>[]</td>
      <td>Madrid</td>
      <td>Milan</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>londON_StockhOlm</td>
      <td>[24, 43, 87]</td>
      <td>London</td>
      <td>Stockholm</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>Budapest_PaRis</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>Brussels_londOn</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>London</td>
    </tr>
  </tbody>
</table>
</div>



# 4


```python
#4 Delete from_to columns

df.drop(columns=['From_To'],inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>RecentDelays</th>
      <th>From</th>
      <th>To</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>[23, 47]</td>
      <td>London</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>[]</td>
      <td>Madrid</td>
      <td>Milan</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>[24, 43, 87]</td>
      <td>London</td>
      <td>Stockholm</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>London</td>
    </tr>
  </tbody>
</table>
</div>



# 5


```python
#5 add new columns of delays

lists = df['RecentDelays'].values
max_size = 0
for lis in lists:
    max_size = max(max_size,len(lis))
max_size
```




    3




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>RecentDelays</th>
      <th>From</th>
      <th>To</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>[23, 47]</td>
      <td>London</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>[]</td>
      <td>Madrid</td>
      <td>Milan</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>[24, 43, 87]</td>
      <td>London</td>
      <td>Stockholm</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>Paris</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>London</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(columns=['delay_1','delay_2','delay_3'],inplace=True)
```


```python
new_lists = list()
for x in range(1,4):
    new_vals = []
    for lis in lists:
        if len(lis) >= x:
            new_vals.append(lis[x-1])
        else :
            new_vals.append(np.nan)
    new_lists.append(new_vals)
df = df.assign(delay_1=new_lists[0])
df = df.assign(delay_2=new_lists[1])
df = df.assign(delay_3=new_lists[2])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>Delays</th>
      <th>From</th>
      <th>To</th>
      <th>delay_1</th>
      <th>delay_2</th>
      <th>delay_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>[23, 47]</td>
      <td>London</td>
      <td>Paris</td>
      <td>23.0</td>
      <td>47.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>[]</td>
      <td>Madrid</td>
      <td>Milan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>[24, 43, 87]</td>
      <td>London</td>
      <td>Stockholm</td>
      <td>24.0</td>
      <td>43.0</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>Paris</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>London</td>
      <td>67.0</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.rename(columns={'RecentDelays':'Delays'},inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Airline</th>
      <th>FlightNumber</th>
      <th>Delays</th>
      <th>From</th>
      <th>To</th>
      <th>delay_1</th>
      <th>delay_2</th>
      <th>delay_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KLM(!)</td>
      <td>10045</td>
      <td>[23, 47]</td>
      <td>London</td>
      <td>Paris</td>
      <td>23.0</td>
      <td>47.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;Air France&gt; (12)</td>
      <td>10055</td>
      <td>[]</td>
      <td>Madrid</td>
      <td>Milan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>(British Airways. )</td>
      <td>10065</td>
      <td>[24, 43, 87]</td>
      <td>London</td>
      <td>Stockholm</td>
      <td>24.0</td>
      <td>43.0</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12. Air France</td>
      <td>10075</td>
      <td>[13]</td>
      <td>Budapest</td>
      <td>Paris</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Swiss Air"</td>
      <td>10085</td>
      <td>[67, 32]</td>
      <td>Brussels</td>
      <td>London</td>
      <td>67.0</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


