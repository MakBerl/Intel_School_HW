import requests

def get_time():
  url="http://worldtimeapi.org/api/timezone/Europe/Moscow"
  resp=requests.get(url)
  unixtime = resp.json()['unixtime']
  return unixtime

def print_time(unixtime):
  print(unixtime)

def main():
  unixtime=get_time()
  print_time(unixtime)

def script_fun():
  try:
    from gt_namespace import pretty_print_mod
    pretty_print_mod.main()
  except ImportError:
    main()