import pandas as pd
def who_drinks_more(filepath):
    data_f=pd.read_csv(filepath)
    fems = data_f[data_f['sex'] == 'F']
    mls = data_f[data_f['sex'] == 'M']
    fem_sum_d = fems['Dalc'].sum()
    fem_sum_w = fems['Walc'].sum()
    sum_fem = fem_sum_w+fem_sum_d
    rows_fems = fems.shape[0]
    average_f=sum_fem/rows_fems
    mls_sum_d = mls['Dalc'].sum()
    mls_sum_w = mls['Walc'].sum()
    sum_mls = mls_sum_w+mls_sum_d
    rows_mls = mls.shape[0]
    average_m=sum_mls/rows_mls
    if average_f>average_m:
        return f'Girls drink more alcohol. Girls - {average_f.round(2)}/5, \
boys - {average_m.round(2)}/5.'
    if average_f<average_m:
        return f'Boys drink more alcohol. Girls - {average_f.round(2)}/5, \
boys - {average_m.round(2)}/5.'
    return f'Boys and girls drink equally({average_f}/5)'

def study_absence(filepath):
    data_f=pd.read_csv(filepath)
    studytime4 = data_f[data_f['studytime'] == 4]
    studytime3 = data_f[data_f['studytime'] == 3]
    studytime2 = data_f[data_f['studytime'] == 2]
    studytime1 = data_f[data_f['studytime'] == 1]
    average4 = studytime4['absences'].mean()
    average3 = studytime3['absences'].mean()
    average2 = studytime2['absences'].mean()
    average1 = studytime1['absences'].mean()
    if average4<=average3<=average2<=average1 or average4>=average3>=average2>=average1:
        return 'There is a connection between class attendance and time spent studying.'
    return 'There is no connection between class attendance and time spent studying.'

def relationships_studies_alcohol(filepath):
    data_f=pd.read_csv(filepath)
    yes = data_f[data_f['romantic'] == 'yes']
    no = data_f[data_f['romantic'] == 'no']
    average_study_yes=yes['absences'].mean()
    average_study_no=no['absences'].mean()
    average_dalc_yes=yes['Dalc'].mean()
    average_walc_yes=yes['Walc'].mean()
    average_dalc_no=no['Dalc'].mean()
    average_walc_no=no['Walc'].mean()
    mean_yes=(average_dalc_yes+average_walc_yes)/2
    mean_no=(average_dalc_no+average_walc_no)/2
    if average_study_yes.round(2)>average_study_no.round(2):
        l='Relationships have a positive impact on learning.'
    if average_study_yes.round(2)<average_study_no.round(2):
        l='Relationships have a negative impact on learning.'
    if average_study_yes.round(2)==average_study_no.round(2):
        l='Relationships have no impact on learning.'
    if mean_yes.round(2)>mean_no.round(2):
        l+=' Relationships make people drunk.'
    if mean_yes.round(2)<mean_no.round(2):
        l+=' There are more drunks without relationships.'
    if mean_no.round(2)==mean_yes.round(2):
        l+=' Relationships do not affect alcohol consumption.'
    return l
