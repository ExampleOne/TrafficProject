import subprocess
import os
import time



sizeMB = os.stat("output_old.avi").st_size / (1024 * 1024.0)

for i in range(250):
    results = open("results_library_p1.txt", 'a')
    starttime = time.time()
    p = subprocess.Popen(["scp", "output2.avi", "videoprocessor@10.226.12.182:videos/"]) # VideoProcessingServer:Desktop/"])
    sts = os.waitpid(p.pid, 0)
    endtime = time.time()
    line = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ' speed of transfer: ' \
                  + str(sizeMB/(endtime - starttime)) + ' time taken: ' + str(endtime - starttime)
    results.write(line + "\n")
    print(line)
    if endtime - starttime < 6:
        time.sleep(6 - (endtime - starttime))
    results.close()




