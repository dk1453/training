import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


xxx = pd.read_csv('/Users/kangdi/Dropbox/quantile regression/archive/loan/loan.csv')
xxx.drop(labels=['annual_inc_joint', 'dti_joint', 'tot_coll_amt', 'tot_cur_bal', 'open_acc_6m', 'open_il_6m',
                 'open_il_12m', 'open_il_24m', 'mths_since_rcnt_il', 'total_bal_il', 'il_util', 'open_rv_12m',
                 'open_rv_24m', 'max_bal_bc', 'all_util', 'total_rev_hi_lim', 'inq_fi', 'total_cu_tl', 'inq_last_12m',
                 'verification_status_joint', 'acc_now_delinq','id', 'member_id', 'sub_grade', 'term', 'emp_title',
                 'emp_length', 'desc', 'issue_d', 'pymnt_plan', 'url', 'purpose', 'title', 'zip_code', 'addr_state',
                 'earliest_cr_line', 'mths_since_last_delinq', 'mths_since_last_record', 'pub_rec', 'loan_status',
                 'initial_list_status', 'last_credit_pull_d', 'last_pymnt_d', 'next_pymnt_d', 'mths_since_last_major_derog',
                 ],
         inplace=True,
         axis=1)
# print(xxx.head())
xxx = xxx.dropna()

xxx['verification_status'] = xxx['verification_status'].replace({
    'Source Verified': 1,
    'Verified': 2,
    'Not Verified': 3
})

xxx['home_ownership'] = xxx['home_ownership'].replace({
    'RENT': 1,
    'OWN': 2,
    'RENT+L14': 3,
    'MORTGAGE': 4,
    'OTHER': 5,
    'NONE': 6,
    'ANY': 7
})

xxx['application_type'] = xxx['application_type'].replace({
    'INDIVIDUAL': 1,
    'JOINT': 2
})

# xxx['loan_status'] = xxx['loan_status'].replace({
#     'Fully Paid': 1,
#     'Charged Off': 2,
#     'Current': 3,
#     'In Grace Period': 4,
#     'Issued': 5,
#     'Late (31-120 days)': 6,
#     'Late (16-30 days)': 7,
#     'Default': 8,
#     'Charged Off': 9
# })

X = xxx.drop('grade', axis=1)
y = xxx['grade']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3906)

log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()

for clf in (log_clf, rnd_clf, svm_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(clf.__class__.__name__, accuracy_score(y_test, y_pred))
