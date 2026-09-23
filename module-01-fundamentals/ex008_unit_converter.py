# Receive a distace value in meters from the keyboard and convert it to float
distace = float(input('Distance in meters: '))

# Convert the distance into different metric units
km = distace / 1000
hm = distace / 100
dam = distace / 10
dm = distace * 10
cm = distace * 100
mm = distace * 1000

# Display the converted values across various metric units
print('The measurement of {}.m corresponds to \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(distace, km, hm, dam, dm, cm, mm))
