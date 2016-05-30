## <  <  <  Bazylek WiFi >  >  >
Python scripts to setup hotspot on Windows 10 and (Windows8/8.1) - > (Not tested).

###Setup Step by Step:
**Step 1.** Download this repository file.

**Step 2.** Run script "run_bazylek.py"
  - python run_bazylek.py
  - python run_bazylek.py -d     <<<<- default
  - python run_bazylek.py [password] 
  - python run_bazylek.py [name] [password]


###**Step 3** only when you setup this first time. 

Step 3. Open "Network and Share Center"
  - Click on "Change adapter settings"
  - Right-click your main ethernet connection and choose “Properties.”
  - Under "Sharing", check all.
  - In Home networking connection dropbox select your "Local Area Connection* 3" or similar
  - Click "OK", and that's all.


You can stop network sharing using secound script "stop_python.py"
  - python stop_bazylek.py
