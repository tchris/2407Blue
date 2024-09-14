import csv
import re
from test import ammotype

text = """Range (yds)	Velocity (fps)	Energy (ft.-lb)	Trajectory (in)	Come Up (moa)	Come Up (mils)	Wind Drift (in)	Wind Drift (moa)	Wind Drift (mils)
0	3358	3004	-1.5	0	0	0	0	0
50	3287	2879	-0.3	0.7	0.2	0.1	0.1	0
100	3218	2759	0	0	0	0.2	0.2	0.1
150	3150	2644	-0.5	0.3	0.1	0.4	0.3	0.1
200	3083	2533	-1.9	0.9	0.3	0.7	0.3	0.1
250	3017	2426	-4.2	1.6	0.5	1.1	0.4	0.1
300	2952	2322	-7.4	2.4	0.7	1.6	0.5	0.1
350	2888	2223	-11.6	3.2	0.9	2.2	0.6	0.2
400	2825	2127	-16.9	4	1.2	2.9	0.7	0.2
450	2763	2035	-23.3	4.9	1.4	3.7	0.8	0.2
500	2702	1946	-30.8	5.9	1.7	4.6	0.9	0.3
550	2642	1860	-39.5	6.9	2	5.6	1	0.3
600	2582	1777	-49.5	7.9	2.3	6.7	1.1	0.3
650	2523	1697	-60.7	8.9	2.6	7.9	1.2	0.3
700	2465	1620	-73.3	10	2.9	9.3	1.3	0.4
750	2408	1545	-87.4	11.1	3.2	10.8	1.4	0.4
800	2352	1473	-102.9	12.3	3.6	12.4	1.5	0.4
850	2296	1404	-120	13.5	3.9	14.2	1.6	0.5
900	2241	1338	-138.8	14.7	4.3	16	1.7	0.5
950	2186	1274	-159.3	16	4.7	18.1	1.8	0.5
1000	2133	1212	-181.6	17.3	5	20.3	1.9	0.6"""
Newformat = text.replace("×", "x")
Newformat = Newformat.replace("–", "-")
Newformat = re.sub(r"\[\d+\]", "", Newformat)
Newformat = Newformat.replace("	", ",")
Newformat = Newformat.splitlines()
data = [line.split(',') for line in Newformat]

csv_file_path = f'TestingDocs/Hornady{ammotype}.csv'



# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)