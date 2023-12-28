import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



alc_stud_health = data_f.loc[: , ["Dalc", "Walc", "health", "studytime"]]
alc_stud_health["alcohol"] = alc_stud_health.Dalc + alc_stud_health.Walc
alc_stud_health.drop(["Dalc", "Walc"], axis = 1, inplace = True)
alc_stud_health

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(alc_stud_health.alcohol, alc_stud_health.studytime, alc_stud_health.health, c=alc_stud_health.health, cmap = "plasma", marker='o')

# Add labels and title
ax.set_xlabel("alcohol consumption")
ax.set_ylabel("study time")
ax.set_zlabel("health")
ax.set_title('3D Scatter Plot Example')

# Show the plot
plt.show()