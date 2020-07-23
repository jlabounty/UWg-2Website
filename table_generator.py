# Faculty
# content= [
#     'David Hertzog  (hertzog@uw.edu)',
#     'Peter Kammel (pkammel@uw.edu)',
#     'Alejandro Garcia (agarcia3@uw.edu)',
#     'Jarek Kaspar (kaspar@uw.edu)',
#     'Martin Fertl (mfertl@uw.edu)',
#     'Erik Swanson (swanson@npl.washington.edu)',
#     'Duncan Prindle (prindle@npl.washington.edu)'
# ]

# Postdocs
content = [
        # 'Kim Siang Khaw (khaw84@uw.edu)',
        # 'Aaron Fienberg (fienberg@uw.edu)',
        # 'Rachel Ryan (rachryan@uw.edu)',
        'Zachary Hodge (zhodge@uw.edu)'
    ]

#Grad Students
content = [
    'Rachel Osofsky (osofskyr@uw.edu)	Muon g-2',
    'Jason Hempstead (hempste2@uw.edu)	Muon g-2',
    "Brynn MacCoy (brynnmaccoy@gmail.com)	Muon g-2",
    'Hannah Binney (hbinney@uw.edu)	Muon g-2',
    'Josh LaBounty (jjlab@uw.edu)	Muon g-2',
    'Ethan Muldoon (ethanm3@uw.edu)	Mu Sun',
]

# for line in content:
#     split = line.replace(")","").replace("(","").split(None)
#     print("<tr>")
#     print("<td>", split[0], split[1],"</td>")
#     print("<td>", split[2],"</td>")
#     print("<td>", split[3], split[4],"</td>")
#     print("</tr>")

content = [
    'Rachel Ryan - 2019 - MuSun - A Precision Measurement of Nuclear Muon Capture in Deuterium with a Cryogenic Time Projection Chamber',
    'Aaron Fienberg - 2019 - Measuring the Precession Frequency in the E989 Muon g-2 experiment',
    'Nathan Froemming - 2018 - Optimization of Muon Injection and Storage in the Fermilab g-2 Experiment: From Simulation to Reality',
    'Matthias Smith - 2017 - Developing the Precision Magnetic Field For the E989 Muon g-2 experiment',
    'Jason Crnkovic - 2013 - Measurement of the e+e- ->pi+pi-pi0 cross section by the radiative return method using Belle Data',
    'Sara Knaack - 2012 - A Determination of the Formation Rate of Muonic Hydrogen Molecules in the MuCap Experiment',
    'Brendan Kiburg - 2011 - A Measurement of the Rate of Muon Capture in an Ultra-Pure Protium Gas Time Projection Chamber',
    'David Webber - 2010 - A Part-Per-Million Measurement of the Positive Muon Lifetime and a Determination of the Fermi Constant',
    'Steven Clayton - 2007 - Measurement of the Rate of Muon Capture in Hydrogen Gas and Determination of the Proton\'s Pseudoscalar Coupling',
    'Dan Chitwood - 2007 - A Measurement of the Mean Life of the Positive Muon to a Precision of 11 Parts per Million',
    'Chris Polly - 2005 - A Measurement of the Anomalous Magnetic Moment of the Negative Muon to 0.7 PPM',
    'Fred Gray - 2003 - A Measurement of the Anomalous Magentic Moment of the Positive Muon with a Precision of 0.7 Parts Per Million',
    'Brian Bunker - 1998 - A Scan of the Cross Section σ(p ̅p⟶ΛΣ^0+c.c.) from Threshold to 2.5 MeV Excess Energy',
    'Johannes Ritter - 1998 - A Measurement of the Reactions pp -> ee, pp -> pi0e and pp -> pi0pi0 from 1.188 GeV/c to 1.445 GeV/c',
    'Paul Reimer - 1996 - A Measurement of the pp -> KsKs Reaction from 0.609 to 1.9 GeV/c',
    'Timothy Jones - 1996 - A Measurement of pp -> LL Near Threshold',
    'Rex Tayloe - 1995 - A Measurement of the pp -> LL and pp -> SL + c.c. Reactions at 1.726 GeV/c',
]

for line in content:
    split = line.split(" - ")
    print("<tr>")
    print("<td>", split[0],"</td>")
    print("<td>", split[1],"</td>")
    print("<td>", *split[2:],"</td>")
    print("</tr>")