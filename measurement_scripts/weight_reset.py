import sys

# This script takes 1 argument:
#
#     1. The filename where the data are saved for then plotting
#         - SynchCounter.txt
#         - loadweight.txt
#         - blockweight.txt
#         - lockweight.txt
#         - sleepweight.txt
#         - SynchCounter_sb.txt
#         - runtimeweight_sb.txt
#         - blockweight_sb.txt
#         - completionweight_sb.txt
#         - schedweight_sb.txt

if __name__ == "__main__":
    with open(str(sys.argv[1]), 'w') as file:
        file.write('0,0' + '\n')
