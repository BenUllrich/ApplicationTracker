import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame([
    {"Company": "Google", "Status": "Submitted"},
    {"Company": "Amazon", "Status": "Interviewing"},
    {"Company": "Meta", "Status": "Rejected"}
])
data['Status'].value_counts().plot(kind='bar')
plt.show()
