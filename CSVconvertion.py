import csv
import re
text = """.17 HM2	2004	US	1[4]	R[5]	4.4×18.1mm	2100[4]	166[4]	0.158		0.172	0.125[5]	18.1mm	Rimfire
.17 HMR	2002	US	4[4][6][7][39]	R[5]	4.5×26.9mm	2525[4]	246[4]	0.195	17[40]	0.172[41]	0.125[5]	26.9mm	Rimfire.
.17 Hornet	1950s [3]	US	2[4][21]	R[10]	4.37×35.31mmR [3]	3629[10]	705[3]	0.389	13.2[10]	0.172[10]		35.31mm	Necked-down .22 Hornet.[3] Watch out for differences between older .17 Ackley Hornet and newer .17 Hornady Hornet. No CIP or SAAMI specs found.
.17 Remington	1971	US	2[2][12]	R	4.4×45.6mm	4123[42]	952[8]	0.462	27[42]	0.172[10]	0.151[12]	45.6mm	
.17 Remington Fireball	2007	US	1[12]	R	4.4×36.1mm	4037[10]	723[8]	0.358	20.5[10]	0.172[10]		36.1mm	High-performance approx 4,000 ft/s (1,200 m/s) in a small case.
.17 WSM	2012	US	3[6][7][43]	R	4.4×31mm	3000[6]	400[6]	0.267		0.172[6]	0.230[6]	31mm	Rimfire.
.22 BR Remington	1963[3]	US		R[3]	5.69×38.15mm[3]	3617[44]	1590[3]	0.879	32.8[3]	0.224[3]	0.415[11]	38.15mm	Wildcat.[3]
.22 Hornet	1930	US	6[4][6][7][12][13][21][22]	R[5]	5.7×35.6mmR	3070[4]	732[4]	0.477	13.0[10]	0.224[10]	0.415[11]	35.6mm	First centerfire cartridge widely adapted for varmint hunting.
.22 Long Rifle	1887[3]	US[3]	6[2][6][7][21][22][39]	R	5.7×15.6mmR	1750	137	0.233	5[3]	0.223		15.6mm	Rimfire. Most common cartridge in the world (by units sold). Black powder propellant charge listed - smokeless likely lower.
.22 PPC	1974	US		R	5.7×38.5mm	3684[10]	1427[8]	0.775	32.0[10]	0.224[10]		38.5mm	
.22 Short	1857[3]	US[3]	3[6][21][22]	H[3]	5.6×11mmR	1164	87	0.149	4[3]	0.222		11mm	Rimfire. Oldest commercial cartridge being loaded today. Black powder propellant charge listed - smokeless likely lower.
.22 WMR	1959	US	6[4][6][7][21][22][39]	R	5.7×26.8mmR	2200[4]	322[4]	0.293		0.224	0.095[5]	26.8mm	Rimfire.
.22-250 Remington	1965	US	7[2][4][6][7][12][13][21]	R[5]	5.7×48.6mm	4545[11]	1776[4]	0.798	43.0[10]	0.224[10]	0.264[5]	48.6mm	Varminter.
.25 ACP	1906	US	6[4][6][7][12][13][21]	H[3]	6.4×15.6mmR	970[10]	73[3]	0.151	1.8[10]	0.251[10]	0.072[5]	15.6mm	Handgun round, popular for small size and weight.[3]
.25 WSSM	2004	US	1[6]	R	6.5×42.4mm	3762[10]	2581[8]	1.372	52.0[10]	0.257[10]	0.418[11]	42.4mm	Winchester Super Short Magnum
.25-06 Remington	1969[3]	US[8]	5[4][6][7][12][13]	R[4]	6.54×63.35mm[8]	3350[4]	2513[4]	1.5	62.0[10]	0.257[10]	0.391[5]	63.35mm	Necked-down 30-06.[3]
.25-20 Winchester	1895	US	2[6][12]	R	6.6×32.8mmR	2101[10]	675[3]	0.643	15[10]	0.257[10]	0.418[11]	32.8mm	.32-20 Winchester case necked down.
.26 Nosler	2013	US	5	R	6.5×65.8mm	3400	3171			0.264[10]		65.8mm	
.28 Nosler	2014	US	2	R	7×65.8mm	3300	3883			0.284[10]		65.78mm	
.30 Carbine	1940	US	6[4][6][7][12][13][21]	R	7.62×33mm	2000[4]	977[4]	0.977	16.0[10]	0.308[10]		33mm	M1 Carbine US service rifle
.30 Herrett	1973	US		H[3]	7.8mm	2270[3]	1470[3]	1.295	27.0[3]	0.308[3]			Wildcat handgun cartridge, based on a shortened .30-30 Winchester.[3]
.30 Nosler	2016	US	2	R	7.62×64.9mm	3200	4092			0.308[10]		64.9mm	
.30 Remington AR	2008	US	1[39]	R[10]	7.849×38.86mm [46]	3076[10]	2208[39]	1.436	40.0[10]	0.308[10]		38.86mm	Billed as "The worlds only 30-caliber big-game cartridge for the light weight AR-15 platform."[39]
.30-06 Springfield	1906	US	8[2][4][6][7][12][13][21][22]	R[5]	7.62×63mm	3080[4]	3178[4]	2.064	62.5[10]	0.308[10]	0.480[5]	63mm	Developed for the U.S. Army's M1903 Springfield rifles prior to WWI. Continued use in the M1 Garand rifle throughout WWII.
.30-30 Winchester	1895	US	6[4][6][7][12][13][21]	R[5]	7.8×51.8mmR	2500[4]	2046[4]	1.637	39[10]	0.308[10]	0.330[5]	51.8mm	a.k.a. .30 Winchester Centerfire and .30 WCF. First smokeless cartridge designed for big game hunting.
.30-40 Krag	1892	US	2[6][12]	R	7.8×58.8mmR	2898[10]	2766[8]	1.909	51[10]	0.308[10]	0.730[11]	58.8mm	Rimmed cartridge.
.30-378 Weatherby Magnum	1959	US[8]		R[10]	7.83×73.99mm[8]	3690[10]	4956[8]	2.686	123.5[10]	0.308[10]	0.730[11]	73.99mm	Belted. Necked-down 378 Weatherby Magnum, developed for 1000-yard performance. Was military-only from 1959 to 1996.
.32 ACP	1899	Belgium	6[4][6][7][12][13][21]	H[3]	7.65×17mm	937[10]	129[3]	0.275	3[10]	0.312[10]	0.090[5]	17mm	.32 Automatic Colt Pistol. a.k.a. .7.65mm Browning.
.32 H&R Magnum	1984	US	2[4][7]	H	7.9×27.3mmR	1150[4]	235[4]	0.409	12.0[10]	0.314[10]		27.3mm	Lengthened .32 S&W Long.
.32 NAA	2002	US	1[4]	H	7.95×17.3mm	1000[4]	178[4]	0.356	5.4[10]	0.311[10]		17.3mm	North American Arms
.32 rimfire	1861	US		H	8×14.6mm	945	159			0.316			a.k.a. .32 Short and .32 Long. Introduced in Smith & Wesson's Model 2 revolver.
.32 S&W	1878	US	2[6][12]	H[3]	7.9×15mmR	595[10]	115[3]	0.387	1.4[10]	0.314[10]		15mm	
.32 S&W Long	1896	US	5[6][7][12][13][21]	H[3]	7.9×23.4mmR	865[10]	132[3]	0.305	3[10]	0.314[10]		23.4mm	Lengthened .32 S&W case.
.32 Winchester Self-Loading	1905	US	0[3]	R[3]	8.2×31mmR	1440[3]	775[3]	1.076	12.5[3]	0.320[3]		31mm	a.k.a. .32 WSL or .32 SL. Obsolete.[3] Only chambered commercially in the Winchester Model 1905 rifle.
.32 Winchester Special	1895[3]	US[8]	4[4][6][7][12]	R[10]	8.18×51.82mmR [8]	2359[10]	1748[8]	1.482	38.5[10]	0.321[10]		51.82mm	Lever action, rimmed. Developed for the Winchester Model 1894.[3]
.32-20 Winchester	1882	US	2[6][12]	R	7.94×33.4mmR	1031[10]	1151[8]	2.233	7.5[10]	0.312[10]		33.4mm	
.33 Nosler	2016	US	3	R	8.6×62.5mm	3025	4589			0.338[11]		64.9mm	
.35 Remington	1906	US	4[4][6][7][12]	R[5]	9.1×49mm	2302[10]	1958[8]	1.701	45.0[10]	0.358[10]	0.300[5]	49mm	Lever action.
.35 Whelen	1922	US	4[2][4][7][12]	R[5]	9.1×63mm	2891[10]	3363[8]	2.327	65.0[10]	0.358[10]	0.282[5]	63mm	Necked up .30-06.
.35 Winchester Self-Loading	1905	US	0[3]	R[3]	8.9×29.3mmR	1452[3]	848[8]	1.168	13.5[3]	0.351[3]		29.3mm	a.k.a. .35 WSL or .35 SL. Obsolete.[3] Only chambered commercially in the Winchester Model 1905 rifle.
.38 Long Colt	1877	US	0[3]	H[3]	9.2×26.2mmR	777[10]	195[3]	0.502	3.7[10]	0.358[10]		26.2mm	a.k.a. .38 LC. Obsolete.[3]
.38 S&W	1877	US	3[6][12][13]	H[3]	9.2×19.7mmR	675[10]	176[3]	0.521	2.6[10]	0.358[10]		19.7mm	4th or 5th oldest commercial cartridge being loaded today.
.38 Special	1902	US	6[4][6][7][12][13][21]	H[13]	9.1×29.3mmR	1090[4]	290[4]	0.532	6.8[10]	0.357[10]	0.206[5]	29.3mm	
.38 Super	1929	US	4[6][7][12][13]	H[3]	9.04×22.86mmR	1300[3]	500[3]	0.769	5.4[3]	0.356[3]		22.86mm	a.k.a. .38 Super and .38 Colt Auto.
.38-40 Winchester	1874[3]	US[8]	1[6]	R[6]	10.17×33.15mmR [8]	1160[6]	538[6]	0.928	19.5[3]	0.401[10]	0.172[6]	33.15mm	aka 38-40 WCF. Crossover rifle/handgun cartridge.[3]
.38-55 Winchester	1884	US	1[6]	R	9.59×53.0mmR	1853[3]	1165[8]	1.257	35.0[3]	0.379[3]		53.00mm	
.40 S&W	1990	US	6[4][6][7][12][13][21]	H	10.2×21.6mm	1180[4]	479[4]	0.812	11.5[10]	0.400[10]	0.164[5]	21.6mm	
.41 Action Express	1986	US		H[3]	10.4×22mm	1114[10]	457[3]	0.82	8.4[10]	0.410[10]		22.0mm	
.41 Long Colt	1877[3]	US	0[3]	H[3]	10.35×28.9mmR	730[3]	235[3]	0.644	3.4[3]	0.410[3]		28.9mm	Obsolete
.41 Remington Magnum	1964	US	3[6][7][12]	H[3]	10.4×32.8mmR	1887[10]	788[3]	0.835	26.5[10]	0.410[10]		32.8mm	
.42 Berdan	1868	Russia		R	10.75×58mmR[3]	1450[3]	1724[3]	2.378	77[3]	0.430[3]		58mm	Black powder Russian service rifle.[3] a.k.a. 4.2 Line Berdan. Designed by American inventor/soldier Hiram Berdan, adopted by Russia in trapdoor 1868 and turnbolt 1870 Berdan Rifles.
.44 AMP	1971	US		H	10.9×33mm	1485[10]	1600[3]	2.155	27.0[10]	0.429[10]			a.k.a. .44 Auto Mag Pistol.
.44 Henry	1860[3]	US	0[3]	R	11×23mmR	1125	568	1.01	28[3]	0.423[24]		23mm	a.k.a. .44 Rimfire, .44 Long Rimfire, or 11×23mmR. Obsolete black powder cartridge.[3]
.44 Magnum	1955	US	6[4][6][7][12][13][21]	H[5]	10.9×32.6mmR	1550[4]	999[4]	1.289	31.5[10]	0.430[10]	0.245[5]	32.6mm	a.k.a. .44 Remington Magnum. Lengthened .44 Special. Crossover rifle/handgun cartridge.[7][12]
.44 Russian	1870[3]	US		H[3]	11×25mmR	770[3]	324[3]	0.842		0.429[3]		25mm	Also known as .44 S&W Russian. Black powder/smokeless handgun cartridge developed from .44 S&W American; developed into .44 Special.[3]
.44 S&W American	1869[3]	US	0[3]	H[3]	11×23mmR	765[3]	259[3]	0.677	5.5[3]	0.434[3]		23mm	Obsolete black powder/smokeless handgun cartridge.[3]
.44 Special	1907[3]	US	4[4][6][7][12]	H[3]	10.9×29mmR	1000[4]	400[4]	0.8	15.0[10]	0.430[10]	0.138[5]	29mm	
.44-40 Winchester	1873[3]	US	2[6][12]	H[3]	10.8×33.3mmR	1117[10]	656[8]	1.175	7.3[10]	0.428[10]	0.123[5]	33.3mm	First developed for lever-action, later used in revolver.[3]
.45 ACP	1905	US	6[4][6][7][12][13][21]	H[5]	11.43×23mm	850[4]	369[4]	0.868	10[10]	0.451[10]	0.188[5]	23mm	Automatic Colt Pistol, first self-loading U.S. Army pistol round.
.45 Colt	1873	US	4[4][6][7][12]	H[5]	11.58×32mm	960[4]	460[4]	0.958	13[10]	0.452[10]	0.140[5]	32mm	a.k.a. .45 Long Colt or .45 LC. Used in both handgun and rifle.
.45 GAP	2003	Austria	3[6][7][12]	H	11.5×19.2mm	1152[10]	543		9.0[10]	0.451[10]		19.2mm	Glock Automatic Pistol.
.45 Raptor	2014	US	2	R	11.5×58mm	3000	3197		48.5	0.452	0.151	58mm	Hybrid of the .460 S&W Magnum and the .308 Winchester. Designed to provide a .45 caliber capability to the AR-10 platform.
.45 Winchester Magnum	1979[3]	US	1[6]	H[3]	11.5×30.4mm	1472[10]	1406[3]	1.91	18.0[10]	0.451[10]		30.4mm	a.k.a. .45 Winchester Magnum. Lengthened and strengthened .45 ACP.
.45-70	1873	US	5[4][6][7][12][13]	R[5]	11.6×53.5mmR	2394[10]	2518[8]	2.104	63[10]	0.458[10]	0.230[5]	53.5mm	a.k.a. .45-70 Government. One of the oldest centerfire cartridges still in commercial production.
.46 rimfire	1870[3]	US		H	11.6×21.2mmR				20[3]	0.456		21.2mm	a.k.a. .46 Short, .46 Remington Carbine. First large-caliber metallic handgun cartridge. Black powder.[3]
.50 Action Express	1988	US	2[4][7]	H[5]	12.7×32.6mm	1475[4]	1449[4]	1.965	32.5[10]	0.500[10]	0.120[5]	32.6mm	For IMI Desert Eagle handgun.
.50 Alaskan	1950s	US		R	13×53mmR	1694	3346	3.95		0.510		53mm	
.50 Beowulf	2001	US		R	12.7×42mm	1800	2878	3.198		0.500		42mm	
.50 BMG	1921	US	2[4][13]	R[5]	12.7×99mm	2815[4]	13196[4]	9.375	265[10]	0.510[10]	1.050[5]	99mm	Used in Heavy Machine Guns and anti-materiel rifles.
.50 GI	2004	US		H	12.7x22.8mm	1200	591	0.985		0.500		22.8mm	Designed to have significantly less recoil than other 50 caliber handguns
.50 Remington Navy	1867[3]	US	0[3]	H[3]	13×21.8mm	750[3]	330[3]	0.88	7.0[3]	0.508[3]		21.8mm	a.k.a. 50 Remington Pistol Navy Model 1867 and 50 Remington (M71 Army). Rimmed case 0.875" in length. Obsolete black powder/smokeless handgun cartridge.[3]
.50-90 Sharps	1872[3]	US		R[3]	13×64mmR	1652[3]	2210[3]	2.676	37.0[3]	0.509[3]		64mm	The mainstay of the American bison (buffalo) hunter. Black powder/smokeless.[3]
.204 Ruger	2004	US	6[2][4][6][7][12][21]	R[5]	5.2×47mm	4456[10]	1351[4]	0.614	31.5[10]	0.204[10]	0.275[5]	47mm	Varmint round.
.218 Bee	1938	US	1[6]	R	5.7×34.2mmR	3545[10]	822[8]	0.464	14.9[10]	0.224[10]		34.2mm	Rimmed.
.220 Swift	1935	US	5[2][4][6][7][12]	R[5]	5.7×56mm	4423[11]	1727[4]	0.897	46.0[10]	0.224[10]	0.264[5]	56.0mm	
.221 Remington Fireball	1963[3]	US	1[12]	H[3]	5.7×35.6mm	3791[10]	780[3]	0.412	22.0[10]	0.224[10]	0.415[11]	35.6mm	Handgun round adapted from 222 Remington.[3]
.222 Remington	1950	US	8[2][4][6][7][12][13][21][22]	R[5]	5.7×43.2mm	3760[4]	1099[4]	0.585	26.2[10]	0.224[10]	0.242[5]	43.2mm	
.223 Remington	1955	US	8[2][4][6][7][12][13][21][22]	R[5]	5.56×45mm	4000[4]	1243[4]	0.622	29.5[10]	0.224[10]	0.395[5]	45mm	Similar but not interchangeable with 5.56NATO.[citation needed]
.223 WSSM	2003	US	1[6]	R	5.7×42.4mm	4568[11]	1918[8]	0.849	50.5[10]	0.224[10]	0.415[11]	42.4mm	Winchester Super Short Magnum
.224 Boz	1997	UK		H	5.56×23mm	2500	694			0.223		23mm	10mm Auto case necked down to 5.56mm.
.224 Weatherby Magnum	1963[3]	US[8]		R[10]	5.70×48.84mm[8]	3865[10]	1704[8]	0.882	36.5[10]	0.224[10]	0.415[11]	48.84mm	Smallest belted magnum case available commercially.[3]
.225 Winchester	1964	US	1[6]	R	5.7×49mmSR	3650[45]	1621	0.888	37.0[45]	0.224	0.415[11]	49.00mm	Semi-rimmed.
.240 Apex	1920	UK	0	R	6.2×63mm	2900	1865			0.245		63mm	aka .240 H&H Magnum Rimless, .240 Magnum Flanged or .240 Super Express
.240 Weatherby Magnum	1968[3]	US[8]		R[10]	6.18×63.50mm[8]	3817[10]	2633[8]	1.38	59.0[10]	0.243[10]		63.50mm	Belted.[8]
.242 Rimless Nitro Express	1923	UK	0	R	6×60mm	2800	1740			0.249-0.253		60mm	aka .242 Manton.
.243 Winchester	1955	US	8[2][4][6][7][12][13][21][22]	R[5]	6.2×51.9mm	3925[4]	2140[4]	1.09	51.0[10]	0.243[10]	0.405[5]	51.9mm	.308 Winchester case necked down to 6mm.
.243 WSSM	2003	US	1[6]	R	6.2×42.4mm	4068[10]	2323[8]	1.142	54.0[10]	0.243[10]	0.525[11]	42.4mm	Winchester Super Short Magnum
.244 H&H Magnum	1955	UK	0	R	6.2x71mm	3500	2720			0.245		71mm	
.244 Halger Magnum	1920	Germany	0	R	6.5×57mm	3270	2142			.243			from Halger Arms Co. of Hamburg
.250-3000 Savage	1915	US	1[12]	R	6.6×48.6mm	3341[10]	2138[8]	1.28	40.5[10]	0.257[10]	0.418[11]	48.6mm	
.256 Winchester Magnum	1962	US	0[3]	H	6.5×32.5mmR	2386[10]	705[3]	0.591	18.0[10]	0.257[10]		32.5mm	.357 Magnum case necked down to .257". a.k.a. 256 Winchester.[10] Obsolete handgun and lever action round.[3]
.257 Roberts	1934[3]	US[8]	4[4][6][7][12]	R[4]	6.55×56.72mm[8]	2946[4]	2255[4]	1.531	54.0[10]	0.257[10]	0.391[5]	56.72mm	
.257 Weatherby Magnum	1944[3]	US[8]	1[4]	R[4]	6.54×64.74mm[8]	3550[4]	2708[4]	1.526	80.0[10]	0.257[10]	0.390[5]	64.74mm	Belted.
.260 Remington	1998[8]	US[8]	2[7][12]	R[10]	6.72×51.69mm[8]	3313[10]	2043[8]	1.233	51.0[10]	0.264[10]	0.719[11]	51.69mm	
.264 Winchester Magnum	1958[3]	US[8]	3[6][12][13]	R[10]	6.73×63.50mm[8]	3863[10]	3020[8]	1.564	78.0[10]	0.264[10]	0.561.[11]	63.50mm	Belted.[8]
.270 Weatherby Magnum	1943[3]	US[8]	1[7]	R[10]	7.04×64.74mm[8]	3647[10]	3639[8]	1.996	81.0[10]	0.277[10]	0.625[11]	64.74mm	Belted.[8] First of Weatherby's line of necked-down 300 H&H-based magnums.[3]
.270 Winchester	1925	US	8[2][4][6][7][12][13][21][22]	R[5]	7.06×64.52mm[8]	3200[4]	2968[4]	1.855	64.0[10]	0.277[10]	0.495[5]	64.52mm	Necked-down .30-06 Springfield.[3]
.270 WSM	2002	US	5[2][6][7][12][22]	R	7.06×53.34mm[8]	3789[10]	3485[8]	1.84	73.0[10]	0.277[10]	0.625.[11]	53.34mm	Winchester Short Magnum
.275 H&H Magnum	1912	UK	0	R	7.3×64mm	2700	2600			0.287		64mm	aka .275 Belted Magnum. Also comes in rimmed version called "Flanged". Necked down .375 H&H Magnum
.280 Ackley Improved	2007	US		R[10]	7.23×64.14mm [46]	3271[10]	3084[11]	1.886	66.0[10]	0.284[10]		64.14mm	Former wildcat now registered by Nosler with SAAMI.
.280 British	1946 [24]	UK		R	7.2×43mm	2549	2019		28.5[24]	0.283[3]		43mm	a.k.a. 7mm FN Short. Intermediate round adopted in 1951.
.280 Jeffery	1913	UK	0	R	7.3×64mm	3000	2800			0.288		64mm	Necked down .333 Jeffery
.280 Remington	1957	US	6[2][4][6][7][12][22]	R[5]	7.2×64.5mm	3433[10]	2899[8]	1.689	64.0[10]	0.284[10]	0.486[5]	64.5mm	.30-06 Springfield case necked down to 7mm.[3]
.280 Ross	1906	Canada	0	R	7.3×66mm	2900	2620			0.287		66mm	.280 Nitro, .280 Rimless Nitro Express Ross (CIP) and .280 Rimless. Once manufactured by Remington and Winchester.
.300 AAC Blackout	2011	US	2[7][13]	R[13]	7.62×35mm	2388[10]	1487[13]	2.05	20.0[10]	0.308[10]		35mm	Developed for suppressed CQB as a sub sonic round. Supersonic is also available.
.300 H&H Magnum	1925[3]	UK[8]	2[4][7]	R[10]	7.82×72.39mm[8]	3394[10]	3485[8]	2.054	81.0[10]	0.308[10]	0.730[11]	72.39mm	Belted. a.k.a. 300 H&H Super a.k.a. Holland's Super 30.[3]
.300 Norma Magnum	2012	US	1[47]	R	7.62×63.3mm	3003	4404			0.308		63.3mm	Necked-down .338 Norma Mag. Selected by US Special Forces in 2016.
.300 Remington Short Action Ultra Magnum	2002[8]	US[8]	1[12]	R[10]	7.85×51.18mm[8]	3663[10]	3761[8]	2.054	69.0[10]	0.308[10]	0.730[11]	51.18mm	Beltless, rebated rim. Remington Short Action Ultra Magnum.
.300 Remington Ultra Magnum	1998[8]	US[8]	2[7][12]	R[10]	7.85×72.39mm[8]	3638[10]	4414[8]	2.427	107.0[10]	0.308[10]	0.730.[11]	72.39mm	Beltless, rebated rim. Fastest cartridge for Nosler's 210-grain AccuBond Long-Range G1=0.730 0.308" bullet.[11]
.300 Ruger Compact Magnum	2007	US	1[4]	R[5]	7.62×53mm	3310[4]	3716[4]	2.245	67.5[10]	0.308[10]	0.480[5]	53mm	Based on .375 Ruger case.
.300 Savage	1920	US	4[4][6][7][12]	R[5]	7.8×47.5mm	2740[4]	2500[4]	1.825	45.2[10]	0.308[10]	0.370[5]	47.5mm	
.300 Weatherby Magnum	1944[3]	US	3[4][7][12]	R[4]	7.8×71.8mm	3375[4]	3890[4]	2.305	90.0[10]	0.308[10]	0.447[5]	71.8mm	
.300 Whisper	2009[8]	US[8]	1[4]	R[4]	7.84×34.90mm[8]	1020[4]	480[4]	0.941	12.0[3]	0.308[10]	0.648[5]	34.90mm	Designed for quiet, accurate, subsonic applications. Year is for homologation by CIP - earlier proprietary and wildcat versions existed.
.300 Winchester Magnum	1963	US	8[2][4][6][7][12][13][21][22]	R[5]	7.8×67mm	3709[10]	3893[4]	2.29	88.0[10]	0.308[10]	0.730[11]	67mm	
.300 WSM	2001	US	5[2][6][7][12][22]	R	7.8×53.5mm	3697[10]	3872[8]	2.095	74.5[10]	0.308[10]	0.730[11]	53.5mm	Winchester Short Magnum
.303 British[48]	1889	UK	7[4][6][7][12][13][21][48]	R[5]	7.7×56mmR	2685[4]	2401[4]	1.788	54[10]	0.311[10]	0.361[5]	56mm	Former British Service rifle Lee–Enfield.
.307 Winchester	1982	US	1[6]	R	7.8×51mmR	3000[10]	2083[8]	1.389	53.0[10]	0.308[10]		51mm	Rimmed version of the .308 Winchester, for use in lever-action rifles.
.308 Marlin Express	2006	US	1[4]	R[5]	7.62×48mm	2800[4]	2514[4]	1.796	47.7[10]	0.308[10]	0.395[5]	48mm	Based upon a slightly shortened .308 Winchester cases with FTX bullets and special powder to approach .308 ballistics from a Marlin lever-action rifle.
.308 Norma Magnum	1960[3]	Sweden[8]	1[2]	R[10]	7.85×65.00mm[8]	3687[10]	3640[8]	1.975	84.0[10]	0.308[10]		65.00mm	Belted. European cartridge designed for the US market.[3]
.308 Winchester	1955	US	8[2][4][6][7][12][13][21][22]	R[5]	7.62×51mm	3358[10]	3009[4]	1.792	54.50[10]	0.308[10]	0.530[5]	51mm	Civilian 7.62mm NATO.
.318 Westley Richards	1910	UK	0	R	8.4×60.1mm	2400	3194			.330		60.1mm	Proprietary cartridge
.325 WSM	2005	US	1[6]	R	8.2×53.3mm	3360[10]	3762[8]	2.239	75.0[10]	0.323[10]		53.3mm	Winchester Short Magnum
.327 Federal Magnum	2008	US	1[7]	H	7.9×30mmR	1600[10]	370[7]	0.463	14.0[10]	0.312[10]		30mm	
.333 Jeffery	1908	UK	0	R	8.5×62.9mm	2500	3230			0.333		62.9mm	Necked down .404 Jeffery
.338 Federal	2007[8]	US[8]	1[7]	R[10]	8.61×51.18mm[8]	2937[10]	3061[8]	2.084	52.0[10]	0.338[10]	0.41[7]	51.18mm	Necked up .308 Win.
.338 Lapua Magnum	1983	Finland	5[4][6][7][13][21]	R[5]	8.6×70mm	2900[4]	4768[4]	3.288	106.0[10]	0.338[10]	0.700[5]	70mm	Designed for military sniper rifles.
.338 Marlin Express	2010[8]	US[8]	1[4]	R[10]	8.60×48.01mmR [8]	2565[4]	2922[4]	2.278	49.3[10]	0.338[10]	0.430[5]	48.01mm	Rimmed lever action cartridge designed for the Marlin Model 336.
.338 Norma Magnum	2008	US	1[49]	R	8.6×63.3mm					0.338		63.3mm	Wildcat designed to derive maximum effect from long, aerodynamic bullets.
.338 Remington Ultra Magnum	2000[8]	US[8]	2[7][12]	R[10]	8.60×70.1mm[8]	3332[10]	4492[8]	2.696	104.0[10]	0.338[10]		70.1mm	Beltless, rebated rim cartridge based on the .300 Remington Ultra Magnum.
.338 Ruger Compact Magnum	2007	US	1[4]	R[5]	8.6×51.2mm	2980[4]	3865[4]	2.594	63.0[10]	0.338[10]	0.515[5]	51.2mm	Based on .375 Ruger case.
.338 Winchester Magnum	1958[3]	US[8]	5[2][4][6][7][12]	R[10]	8.61×63.50mmR [8]	3080[4]	4077[4]	2.647	78.0[10]	0.338[10]	0.515[5]	63.50mm	Belted.[8]
.338-06	1998	US		R	8.6×63mm	2678	3582		62.5	0.338		63mm	Necked up .30-06.
.348 Winchester	1936	US	1[6]	R	8.8×57.3mmR	2630[10]	2685[8]	2.042	70.0[10]	0.348[10]		57.3mm	One of the most powerful rimmed cartridges ever used in a lever rifle.
.350 Legend	2019	US		R[3]	9×43mm	2300	1800		36.5	0.355		43mm	Straight-walled hunting cartridge
.350 Remington Magnum	1965[3]	US[8]	1[12]	R[10]	9.12×55.12mm[8]	2775[12]	3419[12]	2.464	64.5[10]	0.358[10]	0.293[12]	55.12mm	Belted.[8]
.351 Winchester Self-Loading	1906	US		R[3]	8.9×34.9mmR	1850[3]	981[8]	1.061	19.5[3]	0.351[3]		34.9mm	a.k.a. .351 WSL or .351 SL. Only chambered commercially in the Winchester Model 1907 rifle.
.357 Magnum	1935	US	6[4][6][7][12][13][21]	H[13]	9.1×33mmR	1500[4]	624[4]	0.832	23.0[10]	0.357[10]	0.206[5]	33mm	Lengthened .38 Special.
.357 SIG	1994	Germany/US	6[4][6][7][12][13][21]	H[13]	9.02×21.97mm	1350[4]	502[4]	0.744	10.8[10]	0.355[10]	0.212[5]	21.97mm	
.358 Winchester	1955[3]	US[8]	2[4][6]	R[10]	9.11×51.18mm[8]	2475[4]	2720[4]	2.198	52.0[10]	0.358[10]	0.282[5]	51.18mm	
.360 Buckhammer	2023[50]	US[51]	4[51]	R[50]	9.12×62.50mm[50]	2399[52]	2300[53]	1.917		0.359[50]		45.72mm[50]	Introduced by Remington at the 2023 SHOT Show. Straight-walled cartridge based on a blown-out .30-30 Winchester case and designed for deer hunting in U.S. states that require hunters with modern rifles to use that cartridge shape.[51]
.375 Holland & Holland Magnum	1912	UK	7[2][4][6][7][12][13][22]	R[5]	9.5×72.4mm	2800[4]	4700[4]	3.357	87[10]	0.375[10]	0.430[5]	72.4mm	The rimmed .375 H&H Flanged Magnum for double-guns and the .375 H&H Belted Rimless Magnum with a headspacing belt for magazine-fed rifles were released simultaneously in 1912.
.375 Remington Ultra Magnum	2002	US	1[12]	R	9.5×72.4mm	3293[10]	5421[8]	3.292	105.0[10]	0.375[10]		72.4mm	A beltless, rebated rim cartridge developed by Remington Arms by necking up the .300 Remington Ultra Magnum case.
.375 Ruger	2007	US	1[4]	R[5]	9.5×65.5mm	2840[4]	4835[4]	3.405	90.5[10]	0.375[10]	0.430[5]	65.5mm	Developed in collaboration between Ruger and Hornady.[citation needed]
.375 Weatherby Magnum	1945[3]	US		R[3]	9.5×72.6mm	3110[10]	5223[3]	3.359	99.0[10]	0.375[10]		72.6mm	Belted magnum based on the .375 H&H, blown out and reshouldered.[3]
.376 Steyr	1999[3]	Austria & US	2[54]	R	9.5×60mm	2754	4211			0.375		60mm	Hornady and Steyr announced this cartridges at the 2000 Shot Show, based on a concept by Jeff Cooper.[3]
.380 ACP	1912	US	6[4][6][7][12][13][21]	H[13]	9×17mm	1000[4]	200[4]	0.4	4.3[10]	0.355[10]		17mm	a.k.a. .380 Auto, 9mm Browning Short
.400 Corbon	1997	US		H	10.2×23mm	1400	588			0.401		23mm	.45 ACP case necked down to .40 caliber.
.400 H&H Magnum	2003	UK		R	10.4×72.3mm	2375	5015[8]			0.411		72.3mm	Belted magnum.[8]
.401 Winchester Self-Loading	1910	US	0[3]	R[3]	10.31×38mmR	2135[3]	1958[8]	1.834	29.0[3]	0.406[3]		38mm	Rimmed.[8] a.k.a. .401 WSL or .401 SL. Obsolete.[3] Only chambered commercially in the Winchester Model 1910 and the Belgian Clement-Neumann rifle.
.404 Jeffery	1909[3]	UK[8]	3[2][4][22]	R[3]	10.72×73.02mm [8]	2600[3]	4700[3]	3.615	96.4[2]	0.423[3]	0.358[2]	73.02mm	aka 404 Rimless Nitro Express.[8]
.405 Winchester	1904[3]	US[8]	0[3]	R[3]	10.45×65.61mmR [8]	2404[10]	3311[8]	2.936	61.0[10]	0.411[10]		65.61mm	Most powerful rimmed cartridge designed specifically for lever-action rifles. Obsolete.[3]
.408 Cheyenne Tactical	2001	US		R	10.4×77mm	3500	7744[8]			0.408	0.874	77mm	Used in Cheyenne Tactical's M200 Intervention, and M310 rifles.
.416 Barrett	2006	US		R	10.6×83mm	3150	8764	5.564	200	0.416	0.72	83mm	Designed as an alternative to the .50 BMG for sniper rifles.
.416 Remington Magnum	1988	US	5[2][4][6][7][12]	R[5]	10.6×72.4mm	2400[4]	5116[4]	4.263	90.0[10]	0.416[10]	0.367[12]	72.4mm	
.416 Rigby	1911	UK	4[2][4][6][7]	R[5]	10.6×74mm	2415[4]	5180[4]	4.29	116.0[10]	0.416[10]	0.319[5]	74mm	Later used parent cartridge of the .338 Lapua Magnum.
.444 Marlin	1964	US	2[4][12]	R[5]	10.9×57.2mmR	2400[4]	3389[4]	2.824	56.0[10]	0.429[10]	0.225[5]	57.2mm	Lengthened .44 Magnum case, but a lever-action rifle cartridge.
.450 Adams	1868[3]	UK	0[3]	H[3]	11.6×18mmR	700[3]	245[3]	0.7	13[3]	0.455[3]		18mm	a.k.a. .450 Boxer and .450 Revolver. Obsolete black powder handgun cartridge.[3]
.450 Bushmaster	2007	US		R	11.5×43.2mm	2180	2744	2.517		0.452		43.2mm	Developed by hornady as a straight walled rifle round similar to .460 S&W Magnum
.450 Marlin	2000	US	1[4]	R[5]	11.6×53mmR	2225[4]	3572[4]	3.211	59.0[10]	0.458[10]	0.230[5]	53mm	Lever action round. Shortened .458 Winchester Magnum case, designed to match .45-70 performance.
.450 Nitro Express	1895	UK	1[4]	R[5]	12.1×83mmR	2150[4]	4927[4]	4.583	157	0.458[3]	0.325[5]	83mm	J. Rigby smokeless cartridge based upon .450 Black Powder Express.
.454 Casull	1959	US	4[4][6][7][12]	H[5]	11.5×35.1mmR	1900[4]	1924[4]	2.025	38.2[10]	0.452[10]	0.180[5]	35.1mm	Lengthened .45 Colt, most powerful handgun round until the 1990s.
.455 Webley	1897[3]	UK		H[3]	11.5×19.6mmR	700[3]	285[3]	0.814	5.0[3]	0.455[3]		19.6mm	Originally a black powder handgun cartridge.[3]
.458 Lott	1971[3]	US[8]	3[2][4][7]	R[11]	11.66×71.12mm [8]	2300[4]	5873[4]	5.107	79.0[11]	0.458[11]	0.389[11]	71.12mm	Belted.[8]
.458 U.S. Silent Sniper	1969	US	4[2][4][6][7]	R[5]	11.66×33mm	2140[4]	5084[4]	4.751	81.0[10]	0.458[10]	0.295[5]	55mm	Developed for the Silent Sniper System
.458 Winchester Magnum	1956	US	4[2][4][6][7]	R[5]	11.66×64mm	2140[4]	5084[4]	4.751	81.0[10]	0.458[10]	0.295[5]	64mm	
.460 S&W Magnum	2005	US	3[4][6][7]	H[5]	11.5×46mmR	2200[4]	2149[4]	1.954	48.5[10]	0.452[10]	0.151[5]	46mm	Revolver cartridge for handgun hunting.
.460 Weatherby	1958	US		R	11.6×74mm	2808[10]	7504	5.345	128.0[10]	0.458[10]		74mm	aka 460 Weatherby Magnum
.465 H&H Magnum	2003	UK		R	11.9×73.5mm	2375	6121[8]		134	0.468		73.5mm	Belted magnum.[8]
.470 Nitro Express	1907	UK	3[2][4][7]	R[5]	12.1×83mmR	1885[4]	5132[4]	5.445	125[10]	0.475[10]	0.290[5]	83mm	Designed by Joseph Lang.
.475 Linebaugh	1988	US		H	12.1×36mmR	1400	1741	2.487		0.475		36mm	
.476 Enfield	1881[3]	UK		H[3]	11.6m×22mR				5.5[3]	0.472[3]		22mm	a.k.a. .476 Eley. Black powder/smokeless handgun cartridge.[3]
.480 Ruger	2001	US	2[4][7]	H[5]	12.1×32.6mmR	1539[10]	1315	1.709	26.5[10]	0.475[10]	0.150[5]	32.6mm	Shortened .475 Linebaugh case.
.500 Auto Max	2003	US	3[4][6][7]	H[5]	12.7×57.2mm	1950[4]	2533[4]	2.598	45.3[10]	0.500[10]	0.185[5]	57.2mm	Rimmless variant of .500
.500 Linebaugh	1986	US		H	13×35.7mmR	1300	1632	2.511		0.510		35.7mm	
.500 S&W Magnum	2003	US	3[4][6][7]	H[5]	12.7×57.2mmR	1950[4]	2533[4]	2.598	45.3[10]	0.500[10]	0.185[5]	57.2mm	One of the most powerful handgun-specific cartridges.
.505 Gibbs	1910	UK		R	12.8×80mm	2300	6180	5.374		0.505[3]		80mm	
.577 Snider	1867[3]	UK		R	14.5×51mmR	1380[3]	1689[8]	2.448	30[3]	0.570[3]		51mm	The first black powder cartridge for British military use. Later loaded smokeless.[3]
.577/450 Martini–Henry	1871	UK		R	11.43×61mmR	1600[3]	1870[8]	2.338	38[3]	0.455[3]		61mm	Rimmed.[8] The second black powder (later smokeless) cartridge for British military use. Evolved from the .577 Snider case, lengthened and necked down to .45 (nominal) caliber. Used in the Martini rifles from 1871 to the present.
.600 Nitro Express	1899[3]	UK		R[3]	15.7×76mmR	2050[3]	7614[8]	7.428	120[3]	0.622[3]		76mm	Rimmed.[8] Jeffrey, 900-grain (58 g) bullet.[3]
.700 Nitro Express	1988	UK		R[3]	17.8×89mmR	2000[3]	10566[8]	10.566		0.700[3]		89mm	Big game cartridge.
.950 JDJ	2014	US	1	R	24.1x70mm	2200	38685	35.168	3600	0.950		70mm	Largest centerfire rifle cartridge as of 2018
2 mm Kolibri	1914[3]	Austria-Hungary	0[3]	H	2.7×9mm	650[3]	3[3]	0.009		0.108[3]		9mm	Obsolete. Smallest round ever manufactured.[3]
4.6×30mm	2000	Germany		H	4.6×30mm	2410	400	0.332		0.183		30mm	Bottlenecked high velocity PDW cartridge designed by Heckler & Koch in conjunction with the Heckler & Koch MP7 personal defense weapon.
5 mm Remington Rimfire Magnum	1970[3]	US	0[3]	R	5×26mm	2100[3]	327	0.311		0.205[3]		26mm	Obsolete.[3] Rimfire.
5.6mm Gw Pat 90	1987	Switzerland		R	5.56×45mm	3168	1243	0.622	28.5	0.224		45mm	Swiss military version of the 5.56×45mm NATO / 223 Remington. For SIG SG 550 and variants.
5.7×28mm	1990	Belgium	1[7]	R	5.7×28mm	2800	400[8]	0.286	13	0.224		28mm	Bottlenecked high velocity PDW cartridge designed by FN Herstal. Designed in response to NATO requests for a replacement for the 9×19mm cartridge. Frequently used in the FN Five-seven Pistol.
5.8×42mm DBP87	1987	China		R	5.8×42mm	3100	1395	0.9		0.236		42mm	Chinese service rifle QBZ-95
5.45×18mm	1973	USSR	1	H	5.45×18mm	1000	94			0.222		18mm	Developed for PSM pistol.
5.45×39mm	1974	USSR	1[4]	R	5.45×39mm	2810[4]	1052[4]	0.749		0.215		39mm	Developed for AK-74.
5.56×45mm NATO	1960	US		R	5.56×45mm	3130[4]	1196[4]	0.764	28.5	0.224	0.395[5]	45mm	Militarized .223 Rem.
5.56×45mm NATO SS109	1979	Belgium	3[4][6][7]	R	5.56×45mm	2864[4]	1196[4]	0.764	28.5	0.224		45mm	NATO (1980), 2nd gen. Current NATO service including M16 rifle, Steyr AUG, SA80, FAMAS, Heckler & Koch G36. Similar, but not interchangeable with .223 Rem.
6 mm PPC	1975	US		R	6.17×38.5mm	3212[9]	1660[8]	1.034	31.7[9]	0.243[10]	0.376[11]	38.5mm	Benchrest cartridge - "the most accurate round ever developed."[9] .22 PPC case necked up to 6mm.
6.5 Grendel	2003	US	2[4][13]	R	6.5×39mm	2620[4]	1875[4]	1.431	32.0[10]	0.264[10]	0.509[11]	39mm	Developed by Alexander Arms as a "low recoil, high accuracy, long-range cartridge for the AR-15 platform."
6.5-300 Weatherby Magnum	2016	US		R	6.7×72mm	3476	3487			0.264		72mm	
6.5×47mm Lapua	2005	Finland & Switzerland	3[19]	R	6.5×47mm	2900[19]				.264	0.545[20]	50mm	Specifically designed and optimized for 300-1000m competition.[19]
6.5×50mmSR Arisaka	1897	Japan	1[2]	R	6.5×50SR	2717[10]	1966		42[10]	0.264[10]		50mm	aka 6.5×50mm Japanese. Used in Arisaka Japanese service rifles.
6.5×52mm Mannlicher–Carcano	1891	Italy	3[2][13][21]	R	6.50×52mm	2414[10]	1818[8]	1.506	43[10]	0.264[10]		52mm	
6.5×53mmR	1892	Austria-Hungary		R	6.5×53mmR	2650[3]	2360[3]	1.781	38[3]	0.263[3]		53mm	Romanian and Dutch service rifles
6.5×54mm Mauser	1900	Germany		R	6.5×54mm	2362	1468			0.264		54mm	Once chambered for Kurz short-action carbines.
6.5×54mm MS	1908	Austria-Hungary	1[13]	R	6.5×54mm	2395[13]	1987[13]	1.659		0.264		54mm	aka 6.5×54mm Mannlicher–Schönauer "Greek", based on 6.5×53mmR
6.5×55mm	1895	Union of Sweden
and Norway	7[2][4][6][7][13][21][22]	R	6.5×55mm	2735[4]	2325[4]	1.7	52[10]	0.264[10]	0.509[11]	55mm	aka 6.5×55 Swedish Mauser.[2] BC=0.510.[11]
6.5×57mm Mauser	1890	Germany	1[13]	R[13]	6.5×57mm	2772[13]	2099[13]	1.514		0.264		57mm	also 6.5×57mmR. a.k.a. 6.5×57mm RWS. Loaded by Prvi Partizan, RWS, and Sellier & Bellot
6.5×58mm Vergueiro	1904	Portugal		R	6.5×58mm	2775[3]	2372[3]	1.71	46[3]	0.264[3]		58mm	Portuguese service rifle 1904-1939
6.5×68mm	1939	Germany	1[22]	R	6.5×68mm	3700[3]	2983[8]	1.612	73[3]	0.265[3]		68mm	aka 6.5×68mm RWS or Schuler (erroneously)
6.5mm Creedmoor	2012[8]	US[8]	2[4][6]	R[4]	6.72×48.77mm[8]	3050[4]	2493[4]	1.635	47.0[10]	0.264[10]	0.585[5]	48.77mm	
6.5mm JDJ	1978	US		H[3]	6.5mm	2714[3]	1635[3]	1.205	38.5[3]	0.264[3]	0.509[11]		.225 Winchester case necked up to 6.5mm and then blown out.
6.5mm STW[14]	1999	US	0	R	6.5×72.39mm	3300[14]				0.265		72.39mm	Wildcat by Layne Simpson.[14]
6.8mm Remington SPC	2003	US	5[4][7][12][13][21]	R	6.8×43mm	2570[4]	1613[4]	1.255	31.0[10]	0.277[10]	0.370[11]	43mm	Developed by Remington with members of 5th Special Forces Group.
6×57mm Mauser	1895	Germany		R	6×57mm	2600				0.236		57mm	aka 6.2×57mm RWS. Necked down 6.5×57mm. The 6mm Remington is a carbon copy.
6×62mm Freres	1983	Germany	1	R	6×62mm	3460	2260			0.243		62mm	also 6×62mmR, based on 9.3×62mm case.
6mm BR Norma	1996 [14]	Sweden	3[15][16]	R	6x39.6mm	2789[15]				0.243	0.517[15]	39.6mm	Norma's redesigned of the Remington 6mm BR in order to utilize VLD bullets.
6mm Lee Navy	1895	US	0	R	6×60mmSR	2560	1629			0.236		60mm	Service cartridge of the United States Navy and Marine Corps from 1895
6mm Remington	1963[3]	US[8]	5[4][6][7][12][13]	R[4]	6.18×56.72mm[8]	3235[4]	2207[4]	1.364	54.5[10]	0.243[10]	0.405[5]	56.72mm	Same cartridge as .244 Remington and interchangeable. Rifles marked .244 Remington may not stabilize heaviest 6mm Remington bullets.[3]
6mm XC	2000	US	4[17][18]	R	6×48mm	3018[18]	1937			0.243	0.517[18]	48mm	Developed by David Tubb for his Tubb 2000 rifle.
7.5×54mm French	1929	France		R	7.57x54mm	2700	2232		58	0.308		54mm	Case-shortened 7.5×57mm MAS. Standard French rifle cartridge until the introduction of the FAMAS in 1979.
7.5×55mm Swiss	1889[3]	Switzerland	2[2][13]	R	7.5×55mm	2839[10]	2924[8]	2.06	52.0[10]	0.308[10]		55mm	a.k.a. GP-11, 7.5×55mm Schmidt–Rubin.
7.5×57mm MAS	1924	France		R	7.57×57mm	2800[3]	2397[8]	1.712	54[3]	0.308[3]		57mm	8mm Lebel replacement. Rimless rifle cartridge. Same bullet diameter as .30-06. Short-lived due to confusion with 7.92mm Mauser.
7.7×58mm Arisaka	1939	Japan	1[2]	R	7.7×58mm	2529[10]	2510[3]	1.985	55.0[10]	0.311[10]		58mm	aka 7.7×58mm Japanese Arisaka or 31 Jap[3]
7.35×51mm Carcano	1938	Italy		R	7.35×51mm	2550[3]	2175	1.706	41[3]	0.298[3]		51mm	aka 7.35mm Italian Carcano
7.62×25mm Tokarev	1930[3]	USSR[8]	2[13][21]	H[8]	7.90×25mm[8]	1857[21]	650[21]	0.7	10.6[21]	0.311[8]		25.00mm	Based on 7.63×25mm Mauser. Most famous for use in Tokarev TT pistol. Also used in several Soviet submachine guns, including the PPSh-41.
7.62×38mmR	1895	Russia	1[13]	H[13]	7.62×38mmR	1100[3]	290[3]	0.527	3[3]	0.295[3]		38mm	a.k.a. 7.62mm Nagant.
7.62×39mm	1943	USSR	6[4][6][7][12][13][21]	R[13]	7.62×39mm	2360[4]	1521[4]	1.289	31.5[10]	0.312[10]		39mm	Intermediate cartridge concept, following 7.92×33mm Kurz and preceding 5.56×45mm NATO. SKS and AK-47 USSR service rifles.
7.62×51mm NATO	1950	US	2[6][7]	R	7.62×51mm	3165[4]	2997[4]	1.894	54.0[10]	0.308[10]	0.588[11]	51mm	NATO (1953), T65. Current NATO service including M14 rifle, Heckler & Koch G3, FN FAL. Very similar to .308 Win.
7.62×54mmR	1891	Russia	5[2][4][6][13][21]	R[13]	7.62×54mm	2894[2]	2713[4]	1.875	52.6[2]	0.308[2]	0.462.[2]	54mm	Designed for the Mosin–Nagant Russian service rifle. Oldest cartridge still in official military use, used in SVD Dragunov with Russia and the PSL rifles with many other countries.
7.63×25mm Mauser	1893	Germany	1[13]	H[13]	7.62×25mm	1410[3]	375[3]	0.532	6[3]	0.308[3]		25mm	aka 30 Mauser.[3] Based on 7.65×25mm Borchardt. Most famous for use in Mauser C96 pistol. Basis for 7.62×25mm Tokarev round.
7.65×21mm Parabellum	1900	Germany	2[6][13]	H[13]	7.65×21mm	1085[10]	325[3]	0.599	4.2[10]	0.309[10]		21mm	a.k.a. 7.65 Parabellum, 7.65mm Luger, .30 Parabellum and (wrongly) .30 Luger.
7.92×33mm Kurz	1938	Germany	1[13]	R[13]	7.92×33mm	2247[3]	1305[8]	1.162	23[3]	0.323[3]		33mm	First assault rifle round, used in MKb 42.
7.92mm DS	1934	Poland		R	7.92×107mm	4180	8740					107mm	Used for kbk ppanc wz.35 anti-tank rifle.
7×57mm Mauser	1892	Germany	8[2][4][6][7][12][13][21][22]	R[13]	7×57mm	2740[4]	2351[4]	1.716	52.6[3]	0.284[3]	0.531[11]	57mm	aka 7mm Mauser, a.k.a. .275 RIgby
7×64mm	1917[3]	Germany[8]	5[2][12][13][21][22]	R[3]	7.25×64mm[8]	2950[12]	2705[12]	1.834	57.6[2]	0.284[3]	0.450[2]	64.00mm	aka 7×64mm Brenneke.[3]
7×65 R	1917[3]	Germany[8]	2[13][21]	R[21]	7.25×65mmR [8]	2897[21]	3075[8]	2.123	83.6[21]	0.285[8]		65.00mm	aka 7×65mmR Brenneke
7mm BR Remington	1978[3]	US		R	7.21×55.6mm[3]	2425[23]	1525[3]	1.258	34[3]	0.284[3]	0.531[11]	55.6mm	6mm BR necked up to 7mm.[3]
7mm Remington Magnum	1962	US	8[2][4][6][7][12][13][21][22]	R[13]	7.2×64mm	3240[4]	3302[4]	2.038	80.0[10]	0.284[10]	0.652[11]	64mm	
7mm Remington Short Action Ultra Magnum	2004[8]	US[8]	1[12]	R[10]	7.23×51.69mm[8]	3175[12]	3221[12]	2.029	68.0[10]	0.284[10]	0.414[12]	51.69mm	
7mm Remington Ultra Magnum	2002[8]	US[8]	1[12]	R[10]	7.23×72.39mm[8]	3425[12]	3682[12]	2.15	107.0[10]	0.284[10]	0.533[12]	72.39mm	
7mm STW	1981[3]	US[8]	2[7][12]	R[10]	7.23×72.39mm[8]	3325[12]	3436[12]	2.067	91.0[10]	0.284[10]	0.390[12]	72.39mm	Belted.[8]
7mm Weatherby Magnum	1944[3]	US[8]	2[4][7]	R[4]	7.22×64.74mm[8]	3300[4]	3501[4]	2.122	81.8[10]	0.284[10]	0.525[5]	64.74mm	Belted.
7mm WSM	2002	US	2[6][7]	R	7.2×53.3mm	3647[10]	3562[8]	1.953	73.0[10]	0.284[10]	0.531[11]	53.3mm	Winchester Short Magnum
7mm-08 Remington	1980	US	6[2][4][6][7][12][13]	R	7.2×51.7mm	2950[4]	2686[4]	1.821	50.4[10]	0.284[10]	0.531[11]	51.7mm	.308 Winchester case necked down to 7mm.
8×53mmR Murata	1880	Japan		R	8×53mmR	1850[3]	1810[3]	1.957	47.4[24]	0.329[3]		53mm	11×60mm Murata case necked down to 8mm.
8×56mm MS	1908	Austria-Hungary	1[13]	R[13]	8×56mm	2297[13]	2440[13]	2.124		0.323		56mm	Mannlicher–Schönauer
8×57 I	1888[3]	Germany[8]	0	R[8]	8.09×57.00mm[8]	2700	2913[8]			0.318[3]		57.00mm	aka 8×57 J, 7.92×57mm Mauser, 8×57mm Mauser, 8mm Mauser. Original smaller-bore specification. Bullet diameter and chamber pressure were increased in 1905, becoming 8×57 IS. Vintage rifles in this older chambering will dangerously accept modern 8×57 IS.
8×57 IS	1905[3]	Germany[3]	8[2][4][6][7][12][13][21][22]	R	8.22×57.00mm[8]	3208[10]	3171[8]	1.977	57[10]	0.323[10]	0.450[11]	57.00mm	a.k.a. 8×57 JS, 7.92×57mm Mauser, 8×57mm Mauser, 8mm Mauser.[2] Dangerously-similar to the original, smaller-bore 1888 rimless 8×57 I a.k.a. 8×57 J. Also similar to the rimmed 8×57 IRS a.k.a. 8×57 JRS.
8×58mmR Danish Krag	1889	Denmark		R	8x58mm	2500[4]	2720[4]	2.176	54.5[3]	0.322[3]		58mm	aka 8×58mmR Danish Krag.[3] Danish service rifle 1889-1945
8×63mm patron m/32	1932	Sweden	1	R	8×63mm	2500	3025			0.323		63mm	a.k.a. 8x63mm Swedish mg. Used in Swedish machine guns from the 1930s onward.
8×64mm Brenneke	1912	Germany	0	R	8×64mm	2890	3420			0.323		64mm	Also 8x65mmR. Comes in J and S bullets. Based on 9.3x62mm and 9.3x74mmR.
8×68mm S	1939	Germany	2[2][22]	R	8×68mm	3500[3]	3958[3]	2.262	81[3]	0.323[3]	0.450[11]	68mm	aka 8×68Smm Magnum.[3]
8mm Lebel	1886	France		R	8×50mmR	2640[3]	2212[8]	1.676	49[3]	0.323[3]		50mm	a.k.a. 8×50mmR French. Adapted from the 11mm Gras. The first smokeless powder cartridge for military use, started the small-bore smokeless revolution.
8mm Remington Magnum	1978[3]	US[8]	1[12]	R[10]	8.22×72.39mm[8]	2900[12]	3734[12]	2.575	92.0[10]	0.323[10]	0.332[12]	72.39mm	Belted.[8]
8x60mm Mauser	1919	Germany	1[13]	R[13]	8×60mm	2625[13]	2850[13]	2.171		0.323		60mm	aka 8×60mm RWS. Civilian 8mm Mauser. Comes in J and S bullets, rimmed or rimless case. Still loaded by RWS, Prvi Partizan.
9.3×57mm	1900	Sweden	1	R	9.3×57mm	2362	2875			0.365		57mm	Scandinavian 8×57mm variant currently offered by Norma
9.3×62mm	1905	Germany	6[2][4][12][13][21][22]	R[13]	9.3×62mm	2360[4]	3537[4]	2.997	67[10]	0.366[10]	0.494[11]	62mm	Designed by Otto Bock for use in magazine rifles, e.g. Mauser 98, for African game.
9.3×64mm Brenneke	1910	Germany	1[22]	R[22]	9.3×64mm	2576[22]	4317[22]	3.352		0.366	0.465[22]	64mm	
9.3×74mmR	1900[3]	Germany[8]	2[13][21]	R[21]	9.30×74.70mmR [8]	2448[21]	3721[8]	3.04	96.5[21]	0.366[8]		74.70mm	German big-game cartridge.[3]
9.5×57mm MS	1900	UK or Austria-Hungary	0	R	9.5×57mm	2150	2768			0.375		57mm	aka 9.5×56mm Mannlicher–Schönauer, 9.5×56.7mm and .375 Nitro Express Rimless.
9×18mm Makarov	1951	USSR	10[25][26][27][28][29][30][31][32][33]	H	9×18mm	1017[34]	212[34]			0.365[35]		18mm	a.k.a. 9mm Makarov.
9×19mm Parabellum	1901	Germany	6[4][6][7][12][13][21]	H[13]	9×19mm	1155[4]	342[4]	0.592	8.2[10]	0.355[10]	0.212[5]	19mm	a.k.a. 9mm Parabellum, 9mm Para, or 9mm Luger.
9×53mmR	1955	USSR		R	9×53mm	2100	2266					53mm	
9×56mm MS	1900	Austria-Hungary	0	R	9×56mm	2100	2400			0.356		56mm	Mannlicher–Schönauer
9×57mm Mauser	1890	Germany		R	9.06×56.8mm	2423[3]	2692[8]	2.222	46[3]	0.356[3]		56.8mm	Also available in a rimmed version.[3]
9mm Browning Long	1903[3]	Belgium[8]	1[13]	H[13]	9.09×20.20mm[8]	1100[3]	300[3]	0.545	5.0[3]	0.355[3]		20.20mm	Developed for the FN Browning 1903 Model pistol[3]
9mm Mars	1900	UK		H	9.14×26.32mm	1400	675	0.964		0.360		26.32mm	Bottle necked cartridge for the Webley-Mars Automatic Pistol.
10.75×68mm Mauser	1920	Germany	0	R	10.75×68mm	2200	3740			0.424		68mm	Once popular with European hunters in Africa and India. Approaches .375 H&H power with top loads.
10mm Auto	1983[3]	Sweden[8]	5[4][6][7][12][13]	H[8]	10.17×25.20mm [8]	1551[10]	680[3]	0.877	11.2[10]	0.400[10]	0.164[5]	25.20mm	
11×60mm Mauser	1871	Germany		R	11×60mmR	1430[3]	2013[8]	2.815	77[3]	0.446[3]		60mm	The first black powder cartridge adopted in large numbers by the unified German Army, it was used in the 1871 and 1871/84 rifles.
11×60mm Murata	1880	Japan		R	11×60mmR	1487[3]	2063[3]	2.775	77	0.432[3]		60mm	The first black powder cartridge adopted in large numbers by the Japanese Army, it was used in the Murata rifle, a hybrid of French Gras and German Mausers 1871 and 1871/84 rifles.
11mm Gras	1874	France		R	11×59mmR	1493[3]	1903[3]	2.549	78[3]	0.445[3]		59mm	The first French brass cartridge for military use. Black powder.[3] Replaced by 8mm Lebel.[3]
12.7×108mm	1930	USSR		R	12.7×108mm	2700	11980 (13737)		255	0.511		108mm	Used in Heavy Machine Guns, AT-rifles[36] and anti-materiel rifles.
14.5×114mm	1941 [37][38]	USSR		R	14.5×114mm	3300	24520	14.861	1026	0.586		114mm	Used in Heavy Machine Guns, AT-rifles and anti-materiel rifles."""
Newformat = text.replace("×", "x")
Newformat = Newformat.replace("–", "-")
Newformat = re.sub(r"\[\d+\]", "", Newformat)
Newformat = Newformat.replace("	", ",")
Newformat = Newformat.splitlines()
data = [line.split(',') for line in Newformat]

csv_file_path = 'AmmoData.csv'



# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)