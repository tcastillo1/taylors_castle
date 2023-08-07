import pandas as pd
import shutil
import xlwings as xw

# Load pricing metrics file into dataframe
df = pd.read_csv('sample.txt', sep='\t', header=0)

# Get unique list of scenarios from data
scenarios = df['Column1'].unique()
df_summary = pd.DataFrame(columns=['Col1', 'Col2', 'Col3'])

for i in scenarios:

    # Make a copy of the alfa template file for each scenario
    shutil.copy('excel_template.xlsx', 'output_'+str(i)+'.xlsx')

    # Open the copied workbook
    wb = xw.Book('output_'+str(i)+'.xlsx')

    # Get the output sheet
    data_sht = wb.sheets['data']

    # Write the filtered DataFrame to the 'data' sheet starting on 'A2'
    data_sht.range('A2').options(
        index=False, header=True).value = df[df['Column1'] == i]

    # Get the summary data and append it to dataframe
    summary_sht = wb.sheets['summary']
    # Get the summary sheet.
    summary_sht = wb.sheets['Summary']

    # Get the summary data.
    summary_data = summary_sht.range((1, 1), (1, 3)).value

    # Add the summary data to the summary dataframe.
    df_summary = df_summary.append(pd.DataFrame(summary_data, columns=['Col1', 'Col2', 'Col3']), ignore_index=True)
    # Save and close the workbook
    wb.save()
    wb.close()

# Print the summary DataFrame
print(df_summary.head())

# Write the summary DataFrame to a new workbook
summary_wb = xw.Book()
summary_sht = summary_wb.sheets[0]
# summary_sht = summary_wb.sheets['summary']
summary_sht['A1'].options(index=False, header=True).value = df_summary

summary_wb.save('summary_data.xlsx')
summary_wb.close()
