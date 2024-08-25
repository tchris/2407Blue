import csv
import re
from test import ammotype

text = """Range (yds)	Velocity (fps)	Energy (ft.-lb)	Trajectory (in)	Come Up (moa)	Come Up (mils)	Wind Drift (in)	Wind Drift (moa)	Wind Drift (mils)
0	3358	3004	-1.5	0	0	0	0	0
50	3304	2909	-0.3	0.7	0.2	0	0	0
100	3251	2816	0	0	0	0	0	0
150	3199	2726	-0.5	0.3	0.1	0	0	0
200	3147	2639	-1.8	0.9	0.2	0	0	0
250	3096	2554	-4	1.5	0.4	0	0	0
300	3045	2471	-7.1	2.3	0.7	0	0	0
350	2996	2391	-11.1	3	0.9	0	0	0
400	2946	2313	-16.1	3.9	1.1	0	0	0
450	2898	2237	-22.2	4.7	1.4	0	0	0
500	2849	2163	-29.2	5.6	1.6	0	0	0
550	2802	2092	-37.3	6.5	1.9	0	0	0
600	2755	2022	-46.5	7.4	2.2	0	0	0
650	2708	1954	-56.9	8.4	2.4	0	0	0
700	2662	1888	-68.5	9.3	2.7	0	0	0
750	2616	1824	-81.3	10.3	3	0	0	0
800	2571	1761	-95.3	11.4	3.3	0	0	0
850	2526	1701	-110.7	12.4	3.6	0	0	0
900	2482	1642	-127.4	13.5	3.9	0	0	0
950	2438	1584	-145.6	14.6	4.3	0	0	0
1000	2395	1528	-165.2	15.8	4.6	0	0	0
1050	2352	1474	-186.3	16.9	4.9	0	0	0
1100	2309	1421	-209	18.1	5.3	0	0	0
1150	2267	1370	-233.3	19.4	5.6	0	0	0
1200	2225	1320	-259.3	20.6	6	0	0	0
1250	2184	1271	-287.1	21.9	6.4	0	0	0"""
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