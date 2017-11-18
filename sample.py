import sys

from osu.Beatmap import Beatmap
from osu.ctb.difficulty import Difficulty
from ppCalc import calculatePP

if len(sys.argv) <= 1:
    beatmap = Beatmap("test.osu") #Yes... this be my test file (Will remove when project is done)
else:
    beatmap = Beatmap(sys.argv[1])

if len(sys.argv) >= 3:
    mods = int(sys.argv[2])
else:
    mods = 0

difficulty = Difficulty(beatmap, 0)
print("Calculation:")
print("Stars: {}, PP: {}, MaxCombo: {}\n".format(difficulty.starRating, calculatePP(difficulty, 1, beatmap.GetObjectCount(), 0), beatmap.GetObjectCount()))

print("Wanted values:")
print("Stars: 7.4, PP: 784.33, MaxCombo: 2806")
print("HitObjects: 2351, SliderTicks: 455")

"""
m = {"NOMOD": 0, "EASY": 2, "HIDDEN": 8, "HARDROCK": 16, "DOUBLETIME": 64, "HALFTIME": 256, "FLASHLIGHT": 1024}
for key in m.keys():
    difficulty = Difficulty(beatmap, m[key])
    print("Mods: {}".format(key))
    print("Stars: {}".format(difficulty.starRating))
    print("PP: {}\n".format(calculatePP(difficulty, 1, beatmap.GetObjectCount(), 0)))
"""
