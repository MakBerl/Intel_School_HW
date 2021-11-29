from datetime import datetime
from gt_namespace.get_time_mod import  get_time

def print_time_pretty(unixtime):
  formatted_time=datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
  print(formatted_time)

def main():
  unixtime = get_time()
  print_time_pretty(unixtime)

if __name__=='__main__':
  main()
