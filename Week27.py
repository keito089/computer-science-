

def main():
  time = input ("what time is it")                            
  ctime= convert(time)   
  if ctime >=7 and time <=8:
    print("breakfast")
  elif ctime >=12 and time <=13
    print ("lunch")
   elif ctime >=18 and time <=19
    print ("dinner")
    

def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m)
    m = m/60
    return h + m


if __name__ == "__main__":
    main()
