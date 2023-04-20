import re

pattern = r'#+[a-zA-z]*'

data = '#traveler #traveller #traveltheworld #travelblog #traveladdict #mytravelgram #travels #travelphoto #traveldiaries #travellife #travelawesome #travelpics #natgeotravel #travelholic #travelbug #travelstoke #traveldeeper #travelgirl #luxurytravel #worldtraveler #travelers #solotravel #travelpic #travelmore #travellingthroughtheworld #traveldiary #ilovetravel'

result = re.search(pattern, data)
if result:
    print(result.group())
