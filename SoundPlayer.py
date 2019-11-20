import pySonic
import time
      
def finished_stream(source):
  print 'Stream finished playing'

# initialize the audio environment
w = pySonic.World()

# create four sources
bowlsSource = pySonic.Source()
cookingSource = pySonic.Source()
eatingSource = pySonic.Source()
helloSource = pySonic.Source()

# load a sound entirely from disk, stream another from disk
bowlsSource = pySonic.FileSample('./AudioFiles/BowlsOnTable.mp3')
cookingSource = pySonic.FileSample('./AudioFiles/BowlsOnTable.mp3')
eatingSource = pySonic.FileSample('./AudioFiles/BowlsOnTable.mp3')
helloSource = pySonic.FileSample('./AudioFiles/BowlsOnTable.mp3')

# position the sources in 3D space
bowlsSource.Position = (0.0, 0.0, 0.0)
cookingSource.Position = (0.0, 0.0, 0.0)
eatingSource.Position = (0.0, 0.0, 0.0)
helloSource.Position = (0.0, 0.0, 0.0)

# register a callback for when the stream finishes
bowlsSource.SetEndStreamCallback(finished_stream)

# register a callback for when the stream finishes
bowlsSource.Play()

# just block while we're playing in this example
while bowlsSource.IsPlaying():
  time.sleep(1)