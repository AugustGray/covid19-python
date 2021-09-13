import matplotlib.pyplot as plt
import numpy as np

X = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89']
YMexWeekly = [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 34, 119, 553, 971, 2156, 3031, 5997, 7867, 10783, 13510, 17495, 22100, 25399, 29170, 31289, 37907, 36859, 43923, 42124, 46987, 46352, 44770, 41962, 38365, 36004, 37352, 35209, 30655, 31904, 32232, 56661, 31910, 39114, 38036, 36317, 42265, 28576, 64706, 66095, 72609, 72167, 70697, 64942, 70746, 101804, 122555, 109603, 70978, 66083, 51537, 46391, 42423, 38466, 30139, 31935, 27512, 24707, 27785, 23491, 21325, 17119, 16121, 14749, 16034, 20853, 19189, 22921, 26616, 32872, 45911, 64928, 84092, 103283, 114783, 124103, 128799, 114209, 93977, 28217]
YMexTotal = []
ZMexDeathWeekly = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 11, 48, 173, 313, 675, 751, 1188, 1607, 2222, 2426, 3755, 3278, 3948, 5385, 4064, 4348, 4119, 4335, 4043, 4623, 4597, 3702, 3536, 3705, 3332, 2620, 3041, 2648, 5015, 2197, 2608, 2977, 3034, 3301, 3199, 4050, 3990, 4156, 4230, 4588, 4670, 5562, 6953, 8592, 8965, 7711, 8267, 6408, 5509, 5104, 4273, 3368, 3643, 2992, 3166, 4673, 2811, 2403, 1750, 1502, 1097, 1816, 5496, 1255, 1136, 1387, 1079, 1250, 1340, 1939, 2502, 3277, 3681, 4666, 5070, 5071, 1294]
ZMexDeathTotal = []

X_axis = np.arange(len(X))

plt.bar(X_axis, YMexWeekly, 0.6, label = 'Mex Weekly Total', color = "#AA3939")
plt.bar(X_axis, ZMexDeathWeekly, 0.6, label = 'Mex Weekly Deaths', color = "#550000")

plt.title("COVID 19 - Mexico")
plt.legend()
plt.grid()
plt.show()