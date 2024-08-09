import csv
text = """Cartridge,Type,FPS,Energy,Power,Recoil,Length
.17 Aguila	rifle	1850	152	0.37	0.16	0.618
.17 Hornady Magnum Rimfire (HMR)	rifle	2483	246	0.45	0.19	1.06
.17 Mach 2	rifle	2078	163	0.35	0.17	0.714
.17 Remington	rifle	4145	877	0.95	0.45	1.796
.204 Ruger	rifle	3935	1272	1.46	0.6	1.84
.218 Bee	rifle	2760	778	1.27	0.56	1.345
.22 Hornet	rifle	2719	706	1.17	0.54	1.017
.22 Long	rifle	898	52	0.26	0.14	0.613
.22 Long Rifle High Velocity and Hyper Velocity	rifle	1341	152	0.51	0.22	0.613
.22 LR	rifle	1061	99	0.42	0.19	0.613
.22 Short	rifle	896	52	0.26	0.13	0.421
.22 Winchester Magnum Rimfire (WMR)	rifle	2000	342	0.54	0.34	1.055
.22-250 Remington	rifle	3787	1624	1.93	0.9	1.912
.220 Swift	rifle	3845	1674	1.96	0.9	2.205
.221 Remington Fireball	rifle	3097	958	1.39	0.67	1.4
.222 Remington	rifle	3167	1091	1.55	0.74	1.7
.222 Remington Magnum	rifle	3525	1241	1.59	0.79	1.85
.223 Remington (5.56x45mm NATO)	rifle	3148	1254	1.79	0.8	1.76
.223 Winchester Super Short Magnum (WSSM)	rifle	3766	1826	2.18	0.95	1.67
.224 Weatherby Magnum	rifle	3650	1627	2.01	0.9	1.92
.225 Winchester	rifle	3570	1556	1.96	0.9	1.927
.240 Weatherby Magnum	rifle	3396	2432	3.23	1.46	2.5
.243 Winchester	rifle	3179	1952	2.77	1.25	2.045
.243 Winchester Super Short Magnum (WSSM)	rifle	3198	2228	2.55	1.37	1.67
.25 Winchester Super Short Magnum (WSSM)	rifle	3155	2387	3.41	1.57	1.67
.25-06 Remington	rifle	3123	2360	3.4	1.57	2.494
.25-20 Winchester	rifle	1460	407	1.26	0.57	1.33
.25-35 Winchester	rifle	2230	1292	2.61	1.18	2.043
.250 Savage	rifle	2820	1765	2.82	1.27	1.912
.257 Roberts	rifle	2790	2039	3.29	1.47	2.233
.257 Weatherby Magnum	rifle	3408	2836	3.75	1.76	2.549
.260 Remington	rifle	2856	2282	3.6	1.73	2.035
.264 Winchester Magnum	rifle	3170	2766	3.93	1.91	2.5
.270 Weatherby Magnum	rifle	3335	3333	4.5	2.05	2.549
.270 Winchester	rifle	3536	3775	4.81	1.82	2.54
.270 Winchester Short Magnum	rifle	3238	3166	4.4	2	2.1
.280 Remington	rifle	2896	2793	4.34	1.95	2.54
.284 Winchester	rifle	2880	2762	4.32	1.93	2.17
.30 M1 Carbine	rifle	1987	964	2.19	0.99	1.29
.30-06 Springfield	rifle	2815	2920	4.67	2.19	2.494
.30-30 Winchester	rifle	2373	1888	3.58	1.6	2.04
.30-378 Weatherby	rifle	3382	4520	6.02	2.55	2.908
.300 Dakota	rifle	3183	4206	5.95	2.6	2.55
.300 H&H Magnum	rifle	2880	3314	5.18	2.34	2.85
.300 Remington Short Action Ultra Magnum	rifle	3034	3494	5.19	2.36	2.015
.300 Remington Ultra Magnum	rifle	3066	3610	5.3	2.64	2.85
.300 Savage	rifle	2518	2280	4.08	1.78	1.871
.300 Weatherby Magnum	rifle	3229	4074	5.68	2.63	2.811
.300 Winchester Magnum	rifle	3026	3517	5.23	2.39	2.62
.300 Winchester Short Magnum	rifle	3078	3576	5.23	2.36	2.1
.303 British	rifle	2540	2406	4.27	1.98	2.222
.307 Winchester	rifle	2510	2518	4.52	1.93	2.015
.308 Winchester (7.62mm NATO)	rifle	2681	2617	4.4	1.95	2.015
.32 Winchester Special	rifle	2250	1911	3.83	1.95	2.04
.32-20 Winchester	rifle	1210	325	1.21	0.55	1.315
.325 Winchester Short Magnum	rifle	2213	2174	4.43	2.78	2.1
.330 Dakota	rifle	2925	4369	6.73	3.11	2.74
.338 Lapua Magnum	rifle	2927	4831	7.43	3.33	2.774
.338 Winchester Magnum	rifle	2819	3916	6.26	2.93	2.5
.340 Weatherby Magnum	rifle	3033	4615	6.85	3.3	2.825
.35 Remington	rifle	2120	1876	3.99	1.87	1.92
.35 Whelen	rifle	2638	3538	6.04	2.64	2.494
.356 Winchester	rifle	2460	2687	4.92	2.22	2.015
.38-55 Winchester	rifle	1320	986	3.37	1.51	2.085
.44-40 Winchester	rifle	1060	499	2.12	1.07	1.305
.45-70 Government	rifle	1680	2274	6.1	2.43	2.105
.470 Nitro Express	rifle	2134	5055	10.67	4.84	3.25
6.17mm (.243) Lazzeroni Spitfire	rifle	3618	2470	3.08	1.37	2.05
6.53mm (.257) Lazzeroni Scramjet	rifle	3750	3122	3.75	1.69	2.8
6.5mm Remington Magnum	rifle	3118	2655	3.84	1.72	2.17
6.5x55mm Swedish Mauser	rifle	2673	2078	3.5	1.72	2.165
6.5x57 Mauser	rifle	2543	1881	3.33	1.62	2.232
6.8mm Remington SPC	rifle	2600	1696	2.94	1.41	1.686
6mm Remington	rifle	3156	2145	3.06	1.4	2.233
7-30 Waters	rifle	2700	1942	3.24	1.46	2.04
7.62x39mm Russian	rifle	2363	1587	3.02	1.29	1.528
7mm Remington Magnum	rifle	3024	3106	4.63	2.06	2.5
7mm Remington Ultra Magnum	rifle	3121	3330	4.81	2.13	2.85
7mm STW (Shooting Times Westerner)	rifle	3239	3494	4.86	2.31	2.85
7mm Weatherby Magnum	rifle	3199	3476	4.89	2.2	2.549
7mm Winchester Short Magnum (WSM)	rifle	3134	3314	4.76	2.06	2.1
7mm-08 Remington	rifle	2827	2448	3.9	1.8	2.035
7x57mm Mauser	rifle	2602	2255	3.9	1.68	2.235
7x64mm Brenneke	rifle	2818	2662	4.26	1.85	2.51
8mm Remington Magnum	rifle	2900	3734	5.8	2.77	2.85
8x57mm Mauser JS	rifle	2466	2511	4.59	1.81	2.24"""
Newformat = text.replace("	", ",")
Newformat = Newformat.splitlines()
data = [line.split(',') for line in Newformat]

csv_file_path = 'AmmoData.csv'



# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)