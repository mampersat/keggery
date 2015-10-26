A repository to hold random scripts/utilities to interact with the Dyn kegbot api
```
curl -k -v -v -X GET -H "X-Kegbot-Api-Key: <APIKEY>" "http://beer.corp.dyn.com/api/kegs" > kegs.json
```

Current Output:
```
"Harpoon IPA",2015-10-23 13:08:30,2015-10-23 13:08:30,0 days
"Founders Breakfast Stout",2015-10-22 21:32:06,2015-10-22 21:32:06,0 days
"Long Trail Long Trail Ale",2015-10-14 17:04:44,2015-10-22 21:31:30,8 days
"Sierra Nevada Pale Ale",2015-10-08 20:49:33,2015-10-23 13:08:24,14 days
"Anheuser-Busch Bud Light",2015-10-08 20:49:23,2015-10-08 20:49:23,0 days
"Dogfish Head 90min IPA",2015-10-01 20:33:06,2015-10-08 20:49:17,7 days
"Sam Adams Rebel IPA",2015-10-01 20:31:29,2015-10-14 17:04:36,12 days
"Smutty Nose Pumpkin Ale",2015-09-28 20:52:12,2015-10-08 20:49:28,9 days
"Harpoon IPA",2015-09-23 02:08:51,2015-09-28 20:51:36,5 days
"Red Hook Game Changer",2015-09-11 20:28:50,2015-09-23 02:08:43,11 days
"Milly's Raspberry Zeus's Belgian Wit",2015-09-11 16:16:29,2015-10-01 20:31:22,20 days
"Barismo Cambridge Coldbrew",2015-09-02 14:45:39,2015-09-02 14:45:39,0 days
" Smuttynose   Finestkind IPA",2015-08-28 20:19:53,2015-09-11 20:27:58,14 days
"Able Ebenezer Auburn Ale",2015-08-28 20:16:38,2015-08-28 20:16:41,0 days
"Harpoon UFO",2015-08-28 20:09:42,2015-09-11 16:15:02,13 days
"Harpoon UFO",2015-08-28 20:09:39,2015-08-28 20:09:42,0 days
"Harpoon IPA",2015-08-21 21:00:56,2015-08-28 20:04:55,6 days
"Uinta Brewing Co. Hop Nosh IPA",2015-08-14 20:07:38,2015-08-21 21:00:38,7 days
"Anheuser-Busch Bud Light",2015-08-14 20:07:19,2015-10-01 20:32:50,48 days
"Sam Adams Rebel IPA",2015-08-05 21:25:42,2015-08-14 17:06:45,8 days
"Samuel Adams Summer Ale",2015-08-03 20:20:25,2015-08-14 20:05:31,10 days
"Samuel Adams Summer Ale",2015-07-24 20:22:35,2015-07-24 20:22:35,0 days
"Harpoon IPA",2015-07-24 20:22:03,2015-07-24 20:22:03,0 days
"Stark Mill (Milly's) John Stark Porter",2015-07-22 20:54:55,2015-08-28 20:03:40,36 days
"Smuttynose Finestkind IPA ",2015-07-22 20:47:53,2015-08-03 20:20:20,11 days
"Long Trail Long Trail Ale",2015-07-17 19:12:12,2015-07-22 20:54:37,5 days
"Sea Dog Sunfish",2015-07-15 20:42:02,2015-08-05 21:25:15,21 days
"Sam Adams Boston Lager",2015-07-08 12:28:33,2015-07-17 19:11:36,9 days
"Samuel Adams Summer Ale",2015-07-07 18:58:12,2015-07-08 12:28:27,0 days
"Long Trail Long Trail Ale",2015-06-26 18:25:38,2015-07-07 18:58:05,11 days
"Sam Adams Boston Lager",2015-06-25 21:15:45,2015-07-15 20:41:50,19 days
"Sam Adams Boston Lager",2015-06-25 19:58:52,2015-06-26 18:25:31,0 days
"Anheuser-Busch Bud Light",2015-06-18 20:07:31,2015-07-22 20:47:35,34 days
"Harpoon IPA",2015-06-18 20:07:22,2015-06-25 19:58:45,6 days
"Able Ebenezer Burn the Ships",2015-06-15 17:01:26,2015-06-25 21:15:26,10 days
"Samuel Adams Summer Ale",2015-05-29 21:45:30,2015-06-13 16:11:25,14 days
"Anheuser-Busch Bud Light",2015-05-22 18:24:00,2015-06-10 20:39:40,19 days
"Harpoon IPA",2015-05-22 18:23:49,2015-06-09 20:46:02,18 days
"Blue Moon Belgian White",2015-05-15 18:18:48,2015-05-29 21:45:23,14 days
"Harpoon IPA",2015-05-15 18:18:33,2015-05-21 18:05:31,5 days
"Long Trail Long Trail Ale",2015-05-06 21:00:53,2015-05-15 13:23:51,8 days
"Samuel Adams Summer Ale",2015-05-06 21:00:34,2015-05-22 18:23:33,15 days
"Harpoon IPA",2015-04-29 17:53:30,2015-05-06 20:59:18,7 days
"Sea Dog Sunfish",2015-04-27 20:28:59,2015-05-06 21:00:43,9 days
"Anheuser-Busch Bud Light",2015-04-23 19:33:46,2015-05-15 18:18:39,21 days
"Harpoon IPA",2015-04-23 19:33:34,2015-04-27 20:28:08,4 days
"Woodstock Inn Brewery Old Man Oatmeal Stout",2015-04-10 18:10:27,2015-04-23 18:50:53,13 days
"Harpoon IPA",2015-04-10 18:08:56,2015-04-17 16:01:01,6 days
"Lagunitas Pils",2015-04-03 18:28:35,2015-04-10 18:09:14,6 days
"Moat Mountain Brewery Hell Yes!",2015-03-27 21:17:16,2015-04-03 18:26:43,6 days
"Henniker Brewing Working Man's Porter",2015-03-27 21:12:41,2015-04-29 17:53:23,32 days
"Anheuser-Busch Bud Light",2015-03-27 17:44:30,2015-04-10 18:08:41,14 days
"Henniker Brewing Working Man's Porter",2015-03-26 19:41:13,2015-03-27 21:12:15,1 days
"Sam Adams Rebel IPA",2015-03-20 19:42:06,2015-03-26 19:40:40,5 days
"Long Trail Long Trail Ale",2015-03-19 13:50:44,2015-03-27 17:44:23,8 days
"Harpoon IPA",2015-03-13 20:17:47,2015-03-20 19:41:56,6 days
"Brooklyn Brewery Brooklyn Lager",2015-03-12 20:43:09,2015-03-13 20:17:27,0 days
"Redhook ESB",2015-03-12 18:45:46,2015-03-12 20:42:59,0 days
"Smuttynost Robust Porter",2015-03-06 20:52:33,2015-03-27 21:12:35,21 days
"Sam Adams Boston Lager",2015-03-03 19:57:45,2015-03-12 18:45:34,8 days
"Blue Moon Belgian White",2015-02-27 20:20:33,2015-03-03 19:57:26,3 days
"Anheuser-Busch Bud Light",2015-02-27 20:03:48,2015-03-19 13:50:38,19 days
"Brooklyn Brewery Brooklyn Lager",2015-02-23 22:03:30,2015-02-27 20:19:44,3 days
"Harpoon IPA",2015-02-20 20:40:33,2015-03-06 20:51:23,14 days
"Redhook ESB",2015-02-20 20:40:24,2015-02-27 20:02:31,6 days
"Smuttynose IPA ",2015-02-20 20:40:11,2015-02-23 22:02:32,3 days
"Dogfish Head 60min IPA",2015-02-18 22:00:21,2015-02-20 20:40:27,1 days
"Able Ebenezer Burn the Ships",2015-02-13 20:48:46,2015-02-20 20:39:50,6 days
"Throwback Brewery Hopstruck",2015-02-13 20:20:24,2015-02-18 22:00:08,5 days
"Negra Modelo Negra Modelo",2015-02-13 16:27:11,2015-02-20 20:40:16,7 days
"Dogfish Head 60min IPA",2015-02-11 22:19:28,2015-02-13 16:26:57,1 days
"Brooklyn Brewery Brooklyn Lager",2015-02-06 20:54:02,2015-02-11 22:19:14,5 days
"Stone IPA",2015-02-06 20:39:05,2015-02-13 20:19:31,6 days
"Dogfish Head 90min IPA",2015-02-05 18:50:35,2015-02-06 20:38:46,1 days
"North Country Hard Cider Company Original Press",2015-02-05 14:29:57,2015-02-06 20:53:51,1 days
"Negra Modelo Negra Modelo",2015-02-05 02:20:11,2015-02-05 18:50:24,0 days
"Coors Brewing Company Coors Light",2015-02-05 02:17:11,2015-02-13 20:48:39,8 days
"Switchback Switchback Ale",2015-02-04 22:41:06,2015-02-05 14:29:48,0 days
"Dogfish Head 60min IPA",2015-02-03 20:59:08,2015-02-04 21:58:04,1 days
"Harpoon IPA",2015-01-23 20:21:58,2015-02-03 20:58:45,11 days
"Smuttynose Durty",2015-01-22 16:07:19,2015-02-04 22:40:50,13 days
"Uinta Brewing Co. Hop Nosh IPA",2015-01-16 21:38:02,2015-01-23 20:21:43,6 days
"Brooklyn Brewery Brooklyn Lager",2015-01-16 20:23:31,2015-01-22 15:52:05,5 days
"Harpoon IPA",2015-01-12 22:21:10,2015-01-16 21:37:00,3 days
"InBev Stella Artois",2015-01-09 18:31:03,2015-02-05 02:20:01,26 days
"Woodstock Inn Brewery Frosty Goggles",2015-01-07 20:19:35,2015-01-12 22:21:04,5 days
"Brooklyn Brewery Brooklyn Lager",2015-01-05 19:09:32,2015-01-07 20:19:28,2 days
"Dogfish Head 60min IPA",2014-12-30 15:27:41,2015-01-05 19:09:14,6 days
"Sam Adams Octoberfest",2014-12-23 22:16:12,2015-01-16 20:23:22,23 days
"Throwback Brewery Oma's Tribute",2014-12-22 22:00:07,2014-12-23 22:15:54,1 days
"Sierra Nevada Pale Ale",2014-12-19 20:46:02,2014-12-22 21:59:30,3 days
"Throwback Brewery Hopstruck",2014-12-19 20:30:00,2014-12-23 22:16:04,4 days
"Long Trail Long Trail Ale",2014-12-18 21:01:15,2014-12-19 20:29:15,0 days
"Throwback Brewery Chipotle Porter",2014-12-18 21:01:07,2015-01-08 18:51:50,20 days
"Brooklyn Brewery Brooklyn Lager",2014-12-18 19:49:38,2014-12-19 20:45:47,1 days
"Redhook ESB",2014-12-12 21:48:05,2014-12-16 21:39:14,3 days
"Dogfish Head Burton Baton",2014-12-12 20:39:34,2014-12-12 21:47:51,0 days
"Switchback Switchback Ale",2014-12-11 21:18:39,2014-12-12 20:38:56,0 days
"Long Trail Long Trail Ale",2014-12-11 21:03:24,2014-12-18 21:00:49,6 days
"Harpoon IPA",2014-12-04 23:55:06,2014-12-18 14:49:29,13 days
"Guinness Guinness Draught",2014-12-04 19:56:16,2014-12-09 18:32:07,4 days
"Able Ebenezer Auburn Ale",2014-12-04 01:41:45,2014-12-04 23:54:49,0 days
"Henniker Brewing Working Man's Porter",2014-11-21 22:06:05,2014-12-11 21:04:02,19 days
"Dogfish Head 90min IPA",2014-11-21 20:14:34,2014-11-21 22:05:50,0 days
"Henniker Brewing Whipple's Wheat",2014-11-20 19:36:02,2014-12-11 21:02:09,21 days
"Able Ebenezer Burn the Ships",2014-11-14 15:09:57,2014-11-20 19:35:18,6 days
"Sam Adams Winter Lager",2014-11-11 21:30:20,2014-11-21 20:14:24,9 days
"Switchback Switchback Ale",2014-11-07 21:41:21,2014-11-14 15:09:30,6 days
"Dogfish Head 90min IPA",2014-11-07 21:07:59,2014-11-11 21:30:03,4 days
"Dogfish Head 60min IPA",2014-11-07 20:48:35,2014-11-07 21:41:13,0 days
"Dogfish Head 90min IPA",2014-11-07 20:07:41,2014-11-07 20:48:21,0 days
"Dogfish Head 60min IPA",2014-11-06 18:37:03,2014-11-07 20:07:26,1 days
"Sam Adams Octoberfest",2014-11-06 18:36:53,2014-12-04 01:41:36,27 days
"Harpoon IPA",2014-10-31 16:06:01,2014-11-07 21:07:21,7 days
"Switchback Switchback Ale",2014-10-30 21:07:11,2014-11-06 18:36:46,6 days
"Redhook ESB",2014-10-28 20:39:47,2014-10-30 21:06:54,2 days
"Shipyard Pumpkinhead",2014-10-27 20:57:46,2014-10-31 16:05:23,3 days
"Dogfish Head Sixty-One",2014-10-24 20:18:31,2014-10-27 20:57:13,3 days
"Shipyard Pumpkinhead",2014-10-24 19:28:28,2014-10-24 19:28:28,0 days
"Long Trail Long Trail Ale",2014-10-24 19:18:39,2014-11-06 18:36:57,12 days
"Harpoon IPA",2014-10-17 18:40:49,2014-10-28 20:39:43,11 days
"Able Ebenezer Auburn Ale",2014-10-14 20:37:51,2014-10-24 20:18:23,9 days
"Throwback Brewery Donkey-Hote ",2014-10-10 20:19:07,2014-10-14 20:09:35,3 days
"Sam Adams Octoberfest",2014-10-09 13:53:20,2014-10-24 19:18:32,15 days
"Throwback Brewery Hog Happy Hefeweizen",2014-10-09 13:41:55,2014-10-10 20:17:42,1 days
"Throwback Brewery White Heron Chai Porter",2014-10-07 20:48:23,2014-10-09 13:41:50,1 days
"Switchback Switchback Ale",2014-10-06 20:20:32,2014-10-09 13:53:14,2 days
"Shipyard Pumpkinhead",2014-10-06 19:02:21,2014-10-17 18:40:21,10 days
"Dogfish Head 60min IPA",2014-10-06 18:21:29,2014-10-07 20:48:12,1 days

Total: 129 kegs

Harpoon IPA: 17 kegs
{'avg': 7.176470588235294,
 'days': [0, 5, 6, 0, 6, 18, 5, 7, 4, 6, 6, 14, 11, 3, 13, 7, 11],
 'max': 18,
 'min': 0}

Long Trail Long Trail Ale: 8 kegs
{'avg': 7.25, 'days': [8, 5, 11, 8, 8, 0, 6, 12], 'max': 12, 'min': 0}

Anheuser-Busch Bud Light: 7 kegs
{'avg': 22.142857142857142,
 'days': [0, 48, 34, 19, 21, 14, 19],
 'max': 48,
 'min': 0}

Dogfish Head 60min IPA: 7 kegs
{'avg': 1.5714285714285714, 'days': [1, 1, 1, 6, 0, 1, 1], 'max': 6, 'min': 0}

Brooklyn Brewery Brooklyn Lager: 6 kegs
{'avg': 2.6666666666666665, 'days': [0, 3, 5, 5, 2, 1], 'max': 5, 'min': 0}

Dogfish Head 90min IPA: 5 kegs
{'avg': 2.4, 'days': [7, 1, 0, 4, 0], 'max': 7, 'min': 0}

Switchback Switchback Ale: 5 kegs
{'avg': 2.8, 'days': [0, 0, 6, 6, 2], 'max': 6, 'min': 0}

Samuel Adams Summer Ale: 5 kegs
{'avg': 7.8, 'days': [10, 0, 0, 14, 15], 'max': 15, 'min': 0}

Sam Adams Boston Lager: 4 kegs
{'avg': 9.0, 'days': [9, 19, 0, 8], 'max': 19, 'min': 0}

Redhook ESB: 4 kegs
{'avg': 2.75, 'days': [0, 6, 3, 2], 'max': 6, 'min': 0}

Sam Adams Rebel IPA: 3 kegs
{'avg': 8.333333333333334, 'days': [12, 8, 5], 'max': 12, 'min': 5}

Shipyard Pumpkinhead: 3 kegs
{'avg': 4.333333333333333, 'days': [3, 0, 10], 'max': 10, 'min': 0}

Able Ebenezer Burn the Ships: 3 kegs
{'avg': 7.333333333333333, 'days': [10, 6, 6], 'max': 10, 'min': 6}

Sam Adams Octoberfest: 3 kegs
{'avg': 21.666666666666668, 'days': [23, 27, 15], 'max': 27, 'min': 15}

Henniker Brewing Working Man's Porter: 3 kegs
{'avg': 17.333333333333332, 'days': [32, 1, 19], 'max': 32, 'min': 1}

Able Ebenezer Auburn Ale: 3 kegs
{'avg': 3.0, 'days': [0, 0, 9], 'max': 9, 'min': 0}

Sea Dog Sunfish: 2 kegs
{'avg': 15.0, 'days': [21, 9], 'max': 21, 'min': 9}

Uinta Brewing Co. Hop Nosh IPA: 2 kegs
{'avg': 6.5, 'days': [7, 6], 'max': 7, 'min': 6}

Negra Modelo Negra Modelo: 2 kegs
{'avg': 3.5, 'days': [7, 0], 'max': 7, 'min': 0}

Harpoon UFO: 2 kegs
{'avg': 6.5, 'days': [13, 0], 'max': 13, 'min': 0}

Blue Moon Belgian White: 2 kegs
{'avg': 8.5, 'days': [14, 3], 'max': 14, 'min': 3}

Sierra Nevada Pale Ale: 2 kegs
{'avg': 8.5, 'days': [14, 3], 'max': 14, 'min': 3}

Throwback Brewery Hopstruck: 2 kegs
{'avg': 4.5, 'days': [5, 4], 'max': 5, 'min': 4}

Woodstock Inn Brewery Frosty Goggles: 1 kegs
{'avg': 5.0, 'days': [5], 'max': 5, 'min': 5}

Founders Breakfast Stout: 1 kegs
{'avg': 0.0, 'days': [0], 'max': 0, 'min': 0}

Stark Mill (Milly's) John Stark Porter: 1 kegs
{'avg': 36.0, 'days': [36], 'max': 36, 'min': 36}

Dogfish Head Sixty-One: 1 kegs
{'avg': 3.0, 'days': [3], 'max': 3, 'min': 3}

North Country Hard Cider Company Original Press: 1 kegs
{'avg': 1.0, 'days': [1], 'max': 1, 'min': 1}

Milly's Raspberry Zeus's Belgian Wit: 1 kegs
{'avg': 20.0, 'days': [20], 'max': 20, 'min': 20}

Moat Mountain Brewery Hell Yes!: 1 kegs
{'avg': 6.0, 'days': [6], 'max': 6, 'min': 6}

Woodstock Inn Brewery Old Man Oatmeal Stout: 1 kegs
{'avg': 13.0, 'days': [13], 'max': 13, 'min': 13}

Smutty Nose Pumpkin Ale: 1 kegs
{'avg': 9.0, 'days': [9], 'max': 9, 'min': 9}

Dogfish Head Burton Baton: 1 kegs
{'avg': 0.0, 'days': [0], 'max': 0, 'min': 0}

InBev Stella Artois: 1 kegs
{'avg': 26.0, 'days': [26], 'max': 26, 'min': 26}

Throwback Brewery Oma's Tribute: 1 kegs
{'avg': 1.0, 'days': [1], 'max': 1, 'min': 1}

Smuttynost Robust Porter: 1 kegs
{'avg': 21.0, 'days': [21], 'max': 21, 'min': 21}

Smuttynose Finestkind IPA : 1 kegs
{'avg': 11.0, 'days': [11], 'max': 11, 'min': 11}

Throwback Brewery Donkey-Hote : 1 kegs
{'avg': 3.0, 'days': [3], 'max': 3, 'min': 3}

Smuttynose Durty: 1 kegs
{'avg': 13.0, 'days': [13], 'max': 13, 'min': 13}

Henniker Brewing Whipple's Wheat: 1 kegs
{'avg': 21.0, 'days': [21], 'max': 21, 'min': 21}

Throwback Brewery Hog Happy Hefeweizen: 1 kegs
{'avg': 1.0, 'days': [1], 'max': 1, 'min': 1}

Guinness Guinness Draught: 1 kegs
{'avg': 4.0, 'days': [4], 'max': 4, 'min': 4}

Barismo Cambridge Coldbrew: 1 kegs
{'avg': 0.0, 'days': [0], 'max': 0, 'min': 0}

Coors Brewing Company Coors Light: 1 kegs
{'avg': 8.0, 'days': [8], 'max': 8, 'min': 8}

Lagunitas Pils: 1 kegs
{'avg': 6.0, 'days': [6], 'max': 6, 'min': 6}

Throwback Brewery White Heron Chai Porter: 1 kegs
{'avg': 1.0, 'days': [1], 'max': 1, 'min': 1}

 Smuttynose   Finestkind IPA: 1 kegs
{'avg': 14.0, 'days': [14], 'max': 14, 'min': 14}

Stone IPA: 1 kegs
{'avg': 6.0, 'days': [6], 'max': 6, 'min': 6}

Sam Adams Winter Lager: 1 kegs
{'avg': 9.0, 'days': [9], 'max': 9, 'min': 9}

Red Hook Game Changer: 1 kegs
{'avg': 11.0, 'days': [11], 'max': 11, 'min': 11}

Throwback Brewery Chipotle Porter: 1 kegs
{'avg': 20.0, 'days': [20], 'max': 20, 'min': 20}

Smuttynose IPA : 1 kegs
{'avg': 3.0, 'days': [3], 'max': 3, 'min': 3}


{datetime.date(2014, 10, 6): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                           'days': [1,
                                                                    1,
                                                                    1,
                                                                    6,
                                                                    0,
                                                                    1,
                                                                    1],
                                                           'max': 6,
                                                           'min': 0}],
                              u'Shipyard Pumpkinhead': [{'avg': 4.333333333333333,
                                                         'days': [3, 0, 10],
                                                         'max': 10,
                                                         'min': 0}],
                              u'Switchback Switchback Ale': [{'avg': 2.8,
                                                              'days': [0,
                                                                       0,
                                                                       6,
                                                                       6,
                                                                       2],
                                                              'max': 6,
                                                              'min': 0}]},
 datetime.date(2014, 10, 7): {u'Throwback Brewery White Heron Chai Porter': [{'avg': 1.0,
                                                                              'days': [1],
                                                                              'max': 1,
                                                                              'min': 1}]},
 datetime.date(2014, 10, 9): {u'Sam Adams Octoberfest': [{'avg': 21.666666666666668,
                                                          'days': [23,
                                                                   27,
                                                                   15],
                                                          'max': 27,
                                                          'min': 15}],
                              u'Throwback Brewery Hog Happy Hefeweizen': [{'avg': 1.0,
                                                                           'days': [1],
                                                                           'max': 1,
                                                                           'min': 1}]},
 datetime.date(2014, 10, 10): {u'Throwback Brewery Donkey-Hote ': [{'avg': 3.0,
                                                                    'days': [3],
                                                                    'max': 3,
                                                                    'min': 3}]},
 datetime.date(2014, 10, 14): {u'Able Ebenezer Auburn Ale': [{'avg': 3.0,
                                                              'days': [0,
                                                                       0,
                                                                       9],
                                                              'max': 9,
                                                              'min': 0}]},
 datetime.date(2014, 10, 17): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                 'days': [0,
                                                          5,
                                                          6,
                                                          0,
                                                          6,
                                                          18,
                                                          5,
                                                          7,
                                                          4,
                                                          6,
                                                          6,
                                                          14,
                                                          11,
                                                          3,
                                                          13,
                                                          7,
                                                          11],
                                                 'max': 18,
                                                 'min': 0}]},
 datetime.date(2014, 10, 24): {u'Dogfish Head Sixty-One': [{'avg': 3.0,
                                                            'days': [3],
                                                            'max': 3,
                                                            'min': 3}],
                               u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                               'days': [8,
                                                                        5,
                                                                        11,
                                                                        8,
                                                                        8,
                                                                        0,
                                                                        6,
                                                                        12],
                                                               'max': 12,
                                                               'min': 0}],
                               u'Shipyard Pumpkinhead': [{'avg': 4.333333333333333,
                                                          'days': [3,
                                                                   0,
                                                                   10],
                                                          'max': 10,
                                                          'min': 0}]},
 datetime.date(2014, 10, 27): {u'Shipyard Pumpkinhead': [{'avg': 4.333333333333333,
                                                          'days': [3,
                                                                   0,
                                                                   10],
                                                          'max': 10,
                                                          'min': 0}]},
 datetime.date(2014, 10, 28): {u'Redhook ESB': [{'avg': 2.75,
                                                 'days': [0, 6, 3, 2],
                                                 'max': 6,
                                                 'min': 0}]},
 datetime.date(2014, 10, 30): {u'Switchback Switchback Ale': [{'avg': 2.8,
                                                               'days': [0,
                                                                        0,
                                                                        6,
                                                                        6,
                                                                        2],
                                                               'max': 6,
                                                               'min': 0}]},
 datetime.date(2014, 10, 31): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                 'days': [0,
                                                          5,
                                                          6,
                                                          0,
                                                          6,
                                                          18,
                                                          5,
                                                          7,
                                                          4,
                                                          6,
                                                          6,
                                                          14,
                                                          11,
                                                          3,
                                                          13,
                                                          7,
                                                          11],
                                                 'max': 18,
                                                 'min': 0}]},
 datetime.date(2014, 11, 6): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                           'days': [1,
                                                                    1,
                                                                    1,
                                                                    6,
                                                                    0,
                                                                    1,
                                                                    1],
                                                           'max': 6,
                                                           'min': 0}],
                              u'Sam Adams Octoberfest': [{'avg': 21.666666666666668,
                                                          'days': [23,
                                                                   27,
                                                                   15],
                                                          'max': 27,
                                                          'min': 15}]},
 datetime.date(2014, 11, 7): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                           'days': [1,
                                                                    1,
                                                                    1,
                                                                    6,
                                                                    0,
                                                                    1,
                                                                    1],
                                                           'max': 6,
                                                           'min': 0}],
                              u'Dogfish Head 90min IPA': [{'avg': 2.4,
                                                           'days': [7,
                                                                    1,
                                                                    0,
                                                                    4,
                                                                    0],
                                                           'max': 7,
                                                           'min': 0},
                                                          {'avg': 2.4,
                                                           'days': [7,
                                                                    1,
                                                                    0,
                                                                    4,
                                                                    0],
                                                           'max': 7,
                                                           'min': 0}],
                              u'Switchback Switchback Ale': [{'avg': 2.8,
                                                              'days': [0,
                                                                       0,
                                                                       6,
                                                                       6,
                                                                       2],
                                                              'max': 6,
                                                              'min': 0}]},
 datetime.date(2014, 11, 11): {u'Sam Adams Winter Lager': [{'avg': 9.0,
                                                            'days': [9],
                                                            'max': 9,
                                                            'min': 9}]},
 datetime.date(2014, 11, 14): {u'Able Ebenezer Burn the Ships': [{'avg': 7.333333333333333,
                                                                  'days': [10,
                                                                           6,
                                                                           6],
                                                                  'max': 10,
                                                                  'min': 6}]},
 datetime.date(2014, 11, 20): {u"Henniker Brewing Whipple's Wheat": [{'avg': 21.0,
                                                                      'days': [21],
                                                                      'max': 21,
                                                                      'min': 21}]},
 datetime.date(2014, 11, 21): {u'Dogfish Head 90min IPA': [{'avg': 2.4,
                                                            'days': [7,
                                                                     1,
                                                                     0,
                                                                     4,
                                                                     0],
                                                            'max': 7,
                                                            'min': 0}],
                               u"Henniker Brewing Working Man's Porter": [{'avg': 17.333333333333332,
                                                                           'days': [32,
                                                                                    1,
                                                                                    19],
                                                                           'max': 32,
                                                                           'min': 1}]},
 datetime.date(2014, 12, 4): {u'Able Ebenezer Auburn Ale': [{'avg': 3.0,
                                                             'days': [0,
                                                                      0,
                                                                      9],
                                                             'max': 9,
                                                             'min': 0}],
                              u'Guinness Guinness Draught': [{'avg': 4.0,
                                                              'days': [4],
                                                              'max': 4,
                                                              'min': 4}],
                              u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2014, 12, 11): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                               'days': [8,
                                                                        5,
                                                                        11,
                                                                        8,
                                                                        8,
                                                                        0,
                                                                        6,
                                                                        12],
                                                               'max': 12,
                                                               'min': 0}],
                               u'Switchback Switchback Ale': [{'avg': 2.8,
                                                               'days': [0,
                                                                        0,
                                                                        6,
                                                                        6,
                                                                        2],
                                                               'max': 6,
                                                               'min': 0}]},
 datetime.date(2014, 12, 12): {u'Dogfish Head Burton Baton': [{'avg': 0.0,
                                                               'days': [0],
                                                               'max': 0,
                                                               'min': 0}],
                               u'Redhook ESB': [{'avg': 2.75,
                                                 'days': [0, 6, 3, 2],
                                                 'max': 6,
                                                 'min': 0}]},
 datetime.date(2014, 12, 18): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                     'days': [0,
                                                                              3,
                                                                              5,
                                                                              5,
                                                                              2,
                                                                              1],
                                                                     'max': 5,
                                                                     'min': 0}],
                               u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                               'days': [8,
                                                                        5,
                                                                        11,
                                                                        8,
                                                                        8,
                                                                        0,
                                                                        6,
                                                                        12],
                                                               'max': 12,
                                                               'min': 0}],
                               u'Throwback Brewery Chipotle Porter': [{'avg': 20.0,
                                                                       'days': [20],
                                                                       'max': 20,
                                                                       'min': 20}]},
 datetime.date(2014, 12, 19): {u'Sierra Nevada Pale Ale': [{'avg': 8.5,
                                                            'days': [14, 3],
                                                            'max': 14,
                                                            'min': 3}],
                               u'Throwback Brewery Hopstruck': [{'avg': 4.5,
                                                                 'days': [5,
                                                                          4],
                                                                 'max': 5,
                                                                 'min': 4}]},
 datetime.date(2014, 12, 22): {u"Throwback Brewery Oma's Tribute": [{'avg': 1.0,
                                                                     'days': [1],
                                                                     'max': 1,
                                                                     'min': 1}]},
 datetime.date(2014, 12, 23): {u'Sam Adams Octoberfest': [{'avg': 21.666666666666668,
                                                           'days': [23,
                                                                    27,
                                                                    15],
                                                           'max': 27,
                                                           'min': 15}]},
 datetime.date(2014, 12, 30): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                            'days': [1,
                                                                     1,
                                                                     1,
                                                                     6,
                                                                     0,
                                                                     1,
                                                                     1],
                                                            'max': 6,
                                                            'min': 0}]},
 datetime.date(2015, 1, 5): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                   'days': [0,
                                                                            3,
                                                                            5,
                                                                            5,
                                                                            2,
                                                                            1],
                                                                   'max': 5,
                                                                   'min': 0}]},
 datetime.date(2015, 1, 7): {u'Woodstock Inn Brewery Frosty Goggles': [{'avg': 5.0,
                                                                        'days': [5],
                                                                        'max': 5,
                                                                        'min': 5}]},
 datetime.date(2015, 1, 9): {u'InBev Stella Artois': [{'avg': 26.0,
                                                       'days': [26],
                                                       'max': 26,
                                                       'min': 26}]},
 datetime.date(2015, 1, 12): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 1, 16): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                    'days': [0,
                                                                             3,
                                                                             5,
                                                                             5,
                                                                             2,
                                                                             1],
                                                                    'max': 5,
                                                                    'min': 0}],
                              u'Uinta Brewing Co. Hop Nosh IPA': [{'avg': 6.5,
                                                                   'days': [7,
                                                                            6],
                                                                   'max': 7,
                                                                   'min': 6}]},
 datetime.date(2015, 1, 22): {u'Smuttynose Durty': [{'avg': 13.0,
                                                     'days': [13],
                                                     'max': 13,
                                                     'min': 13}]},
 datetime.date(2015, 1, 23): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 2, 3): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                          'days': [1,
                                                                   1,
                                                                   1,
                                                                   6,
                                                                   0,
                                                                   1,
                                                                   1],
                                                          'max': 6,
                                                          'min': 0}]},
 datetime.date(2015, 2, 4): {u'Switchback Switchback Ale': [{'avg': 2.8,
                                                             'days': [0,
                                                                      0,
                                                                      6,
                                                                      6,
                                                                      2],
                                                             'max': 6,
                                                             'min': 0}]},
 datetime.date(2015, 2, 5): {u'Coors Brewing Company Coors Light': [{'avg': 8.0,
                                                                     'days': [8],
                                                                     'max': 8,
                                                                     'min': 8}],
                             u'Dogfish Head 90min IPA': [{'avg': 2.4,
                                                          'days': [7,
                                                                   1,
                                                                   0,
                                                                   4,
                                                                   0],
                                                          'max': 7,
                                                          'min': 0}],
                             u'Negra Modelo Negra Modelo': [{'avg': 3.5,
                                                             'days': [7, 0],
                                                             'max': 7,
                                                             'min': 0}],
                             u'North Country Hard Cider Company Original Press': [{'avg': 1.0,
                                                                                   'days': [1],
                                                                                   'max': 1,
                                                                                   'min': 1}]},
 datetime.date(2015, 2, 6): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                   'days': [0,
                                                                            3,
                                                                            5,
                                                                            5,
                                                                            2,
                                                                            1],
                                                                   'max': 5,
                                                                   'min': 0}],
                             u'Stone IPA': [{'avg': 6.0,
                                             'days': [6],
                                             'max': 6,
                                             'min': 6}]},
 datetime.date(2015, 2, 11): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                           'days': [1,
                                                                    1,
                                                                    1,
                                                                    6,
                                                                    0,
                                                                    1,
                                                                    1],
                                                           'max': 6,
                                                           'min': 0}]},
 datetime.date(2015, 2, 13): {u'Able Ebenezer Burn the Ships': [{'avg': 7.333333333333333,
                                                                 'days': [10,
                                                                          6,
                                                                          6],
                                                                 'max': 10,
                                                                 'min': 6}],
                              u'Negra Modelo Negra Modelo': [{'avg': 3.5,
                                                              'days': [7,
                                                                       0],
                                                              'max': 7,
                                                              'min': 0}],
                              u'Throwback Brewery Hopstruck': [{'avg': 4.5,
                                                                'days': [5,
                                                                         4],
                                                                'max': 5,
                                                                'min': 4}]},
 datetime.date(2015, 2, 18): {u'Dogfish Head 60min IPA': [{'avg': 1.5714285714285714,
                                                           'days': [1,
                                                                    1,
                                                                    1,
                                                                    6,
                                                                    0,
                                                                    1,
                                                                    1],
                                                           'max': 6,
                                                           'min': 0}]},
 datetime.date(2015, 2, 20): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}],
                              u'Redhook ESB': [{'avg': 2.75,
                                                'days': [0, 6, 3, 2],
                                                'max': 6,
                                                'min': 0}],
                              u'Smuttynose IPA ': [{'avg': 3.0,
                                                    'days': [3],
                                                    'max': 3,
                                                    'min': 3}]},
 datetime.date(2015, 2, 23): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                    'days': [0,
                                                                             3,
                                                                             5,
                                                                             5,
                                                                             2,
                                                                             1],
                                                                    'max': 5,
                                                                    'min': 0}]},
 datetime.date(2015, 2, 27): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Blue Moon Belgian White': [{'avg': 8.5,
                                                            'days': [14, 3],
                                                            'max': 14,
                                                            'min': 3}]},
 datetime.date(2015, 3, 3): {u'Sam Adams Boston Lager': [{'avg': 9.0,
                                                          'days': [9,
                                                                   19,
                                                                   0,
                                                                   8],
                                                          'max': 19,
                                                          'min': 0}]},
 datetime.date(2015, 3, 6): {u'Smuttynost Robust Porter': [{'avg': 21.0,
                                                            'days': [21],
                                                            'max': 21,
                                                            'min': 21}]},
 datetime.date(2015, 3, 12): {u'Brooklyn Brewery Brooklyn Lager': [{'avg': 2.6666666666666665,
                                                                    'days': [0,
                                                                             3,
                                                                             5,
                                                                             5,
                                                                             2,
                                                                             1],
                                                                    'max': 5,
                                                                    'min': 0}],
                              u'Redhook ESB': [{'avg': 2.75,
                                                'days': [0, 6, 3, 2],
                                                'max': 6,
                                                'min': 0}]},
 datetime.date(2015, 3, 13): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 3, 19): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                              'days': [8,
                                                                       5,
                                                                       11,
                                                                       8,
                                                                       8,
                                                                       0,
                                                                       6,
                                                                       12],
                                                              'max': 12,
                                                              'min': 0}]},
 datetime.date(2015, 3, 20): {u'Sam Adams Rebel IPA': [{'avg': 8.333333333333334,
                                                        'days': [12, 8, 5],
                                                        'max': 12,
                                                        'min': 5}]},
 datetime.date(2015, 3, 26): {u"Henniker Brewing Working Man's Porter": [{'avg': 17.333333333333332,
                                                                          'days': [32,
                                                                                   1,
                                                                                   19],
                                                                          'max': 32,
                                                                          'min': 1}]},
 datetime.date(2015, 3, 27): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u"Henniker Brewing Working Man's Porter": [{'avg': 17.333333333333332,
                                                                          'days': [32,
                                                                                   1,
                                                                                   19],
                                                                          'max': 32,
                                                                          'min': 1}],
                              u'Moat Mountain Brewery Hell Yes!': [{'avg': 6.0,
                                                                    'days': [6],
                                                                    'max': 6,
                                                                    'min': 6}]},
 datetime.date(2015, 4, 3): {u'Lagunitas Pils': [{'avg': 6.0,
                                                  'days': [6],
                                                  'max': 6,
                                                  'min': 6}]},
 datetime.date(2015, 4, 10): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}],
                              u'Woodstock Inn Brewery Old Man Oatmeal Stout': [{'avg': 13.0,
                                                                                'days': [13],
                                                                                'max': 13,
                                                                                'min': 13}]},
 datetime.date(2015, 4, 23): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 4, 27): {u'Sea Dog Sunfish': [{'avg': 15.0,
                                                    'days': [21, 9],
                                                    'max': 21,
                                                    'min': 9}]},
 datetime.date(2015, 4, 29): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 5, 6): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                             'days': [8,
                                                                      5,
                                                                      11,
                                                                      8,
                                                                      8,
                                                                      0,
                                                                      6,
                                                                      12],
                                                             'max': 12,
                                                             'min': 0}],
                             u'Samuel Adams Summer Ale': [{'avg': 7.8,
                                                           'days': [10,
                                                                    0,
                                                                    0,
                                                                    14,
                                                                    15],
                                                           'max': 15,
                                                           'min': 0}]},
 datetime.date(2015, 5, 15): {u'Blue Moon Belgian White': [{'avg': 8.5,
                                                            'days': [14, 3],
                                                            'max': 14,
                                                            'min': 3}],
                              u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 5, 22): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 5, 29): {u'Samuel Adams Summer Ale': [{'avg': 7.8,
                                                            'days': [10,
                                                                     0,
                                                                     0,
                                                                     14,
                                                                     15],
                                                            'max': 15,
                                                            'min': 0}]},
 datetime.date(2015, 6, 15): {u'Able Ebenezer Burn the Ships': [{'avg': 7.333333333333333,
                                                                 'days': [10,
                                                                          6,
                                                                          6],
                                                                 'max': 10,
                                                                 'min': 6}]},
 datetime.date(2015, 6, 18): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 6, 25): {u'Sam Adams Boston Lager': [{'avg': 9.0,
                                                           'days': [9,
                                                                    19,
                                                                    0,
                                                                    8],
                                                           'max': 19,
                                                           'min': 0},
                                                          {'avg': 9.0,
                                                           'days': [9,
                                                                    19,
                                                                    0,
                                                                    8],
                                                           'max': 19,
                                                           'min': 0}]},
 datetime.date(2015, 6, 26): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                              'days': [8,
                                                                       5,
                                                                       11,
                                                                       8,
                                                                       8,
                                                                       0,
                                                                       6,
                                                                       12],
                                                              'max': 12,
                                                              'min': 0}]},
 datetime.date(2015, 7, 7): {u'Samuel Adams Summer Ale': [{'avg': 7.8,
                                                           'days': [10,
                                                                    0,
                                                                    0,
                                                                    14,
                                                                    15],
                                                           'max': 15,
                                                           'min': 0}]},
 datetime.date(2015, 7, 8): {u'Sam Adams Boston Lager': [{'avg': 9.0,
                                                          'days': [9,
                                                                   19,
                                                                   0,
                                                                   8],
                                                          'max': 19,
                                                          'min': 0}]},
 datetime.date(2015, 7, 15): {u'Sea Dog Sunfish': [{'avg': 15.0,
                                                    'days': [21, 9],
                                                    'max': 21,
                                                    'min': 9}]},
 datetime.date(2015, 7, 17): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                              'days': [8,
                                                                       5,
                                                                       11,
                                                                       8,
                                                                       8,
                                                                       0,
                                                                       6,
                                                                       12],
                                                              'max': 12,
                                                              'min': 0}]},
 datetime.date(2015, 7, 22): {u'Smuttynose Finestkind IPA ': [{'avg': 11.0,
                                                               'days': [11],
                                                               'max': 11,
                                                               'min': 11}],
                              u"Stark Mill (Milly's) John Stark Porter": [{'avg': 36.0,
                                                                           'days': [36],
                                                                           'max': 36,
                                                                           'min': 36}]},
 datetime.date(2015, 7, 24): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}],
                              u'Samuel Adams Summer Ale': [{'avg': 7.8,
                                                            'days': [10,
                                                                     0,
                                                                     0,
                                                                     14,
                                                                     15],
                                                            'max': 15,
                                                            'min': 0}]},
 datetime.date(2015, 8, 3): {u'Samuel Adams Summer Ale': [{'avg': 7.8,
                                                           'days': [10,
                                                                    0,
                                                                    0,
                                                                    14,
                                                                    15],
                                                           'max': 15,
                                                           'min': 0}]},
 datetime.date(2015, 8, 5): {u'Sam Adams Rebel IPA': [{'avg': 8.333333333333334,
                                                       'days': [12, 8, 5],
                                                       'max': 12,
                                                       'min': 5}]},
 datetime.date(2015, 8, 14): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Uinta Brewing Co. Hop Nosh IPA': [{'avg': 6.5,
                                                                   'days': [7,
                                                                            6],
                                                                   'max': 7,
                                                                   'min': 6}]},
 datetime.date(2015, 8, 21): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 8, 28): {u' Smuttynose   Finestkind IPA': [{'avg': 14.0,
                                                                 'days': [14],
                                                                 'max': 14,
                                                                 'min': 14}],
                              u'Able Ebenezer Auburn Ale': [{'avg': 3.0,
                                                             'days': [0,
                                                                      0,
                                                                      9],
                                                             'max': 9,
                                                             'min': 0}],
                              u'Harpoon UFO': [{'avg': 6.5,
                                                'days': [13, 0],
                                                'max': 13,
                                                'min': 0},
                                               {'avg': 6.5,
                                                'days': [13, 0],
                                                'max': 13,
                                                'min': 0}]},
 datetime.date(2015, 9, 2): {u'Barismo Cambridge Coldbrew': [{'avg': 0.0,
                                                              'days': [0],
                                                              'max': 0,
                                                              'min': 0}]},
 datetime.date(2015, 9, 11): {u"Milly's Raspberry Zeus's Belgian Wit": [{'avg': 20.0,
                                                                         'days': [20],
                                                                         'max': 20,
                                                                         'min': 20}],
                              u'Red Hook Game Changer': [{'avg': 11.0,
                                                          'days': [11],
                                                          'max': 11,
                                                          'min': 11}]},
 datetime.date(2015, 9, 23): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                'days': [0,
                                                         5,
                                                         6,
                                                         0,
                                                         6,
                                                         18,
                                                         5,
                                                         7,
                                                         4,
                                                         6,
                                                         6,
                                                         14,
                                                         11,
                                                         3,
                                                         13,
                                                         7,
                                                         11],
                                                'max': 18,
                                                'min': 0}]},
 datetime.date(2015, 9, 28): {u'Smutty Nose Pumpkin Ale': [{'avg': 9.0,
                                                            'days': [9],
                                                            'max': 9,
                                                            'min': 9}]},
 datetime.date(2015, 10, 1): {u'Dogfish Head 90min IPA': [{'avg': 2.4,
                                                           'days': [7,
                                                                    1,
                                                                    0,
                                                                    4,
                                                                    0],
                                                           'max': 7,
                                                           'min': 0}],
                              u'Sam Adams Rebel IPA': [{'avg': 8.333333333333334,
                                                        'days': [12, 8, 5],
                                                        'max': 12,
                                                        'min': 5}]},
 datetime.date(2015, 10, 8): {u'Anheuser-Busch Bud Light': [{'avg': 22.142857142857142,
                                                             'days': [0,
                                                                      48,
                                                                      34,
                                                                      19,
                                                                      21,
                                                                      14,
                                                                      19],
                                                             'max': 48,
                                                             'min': 0}],
                              u'Sierra Nevada Pale Ale': [{'avg': 8.5,
                                                           'days': [14, 3],
                                                           'max': 14,
                                                           'min': 3}]},
 datetime.date(2015, 10, 14): {u'Long Trail Long Trail Ale': [{'avg': 7.25,
                                                               'days': [8,
                                                                        5,
                                                                        11,
                                                                        8,
                                                                        8,
                                                                        0,
                                                                        6,
                                                                        12],
                                                               'max': 12,
                                                               'min': 0}]},
 datetime.date(2015, 10, 22): {u'Founders Breakfast Stout': [{'avg': 0.0,
                                                              'days': [0],
                                                              'max': 0,
                                                              'min': 0}]},
 datetime.date(2015, 10, 23): {u'Harpoon IPA': [{'avg': 7.176470588235294,
                                                 'days': [0,
                                                          5,
                                                          6,
                                                          0,
                                                          6,
                                                          18,
                                                          5,
                                                          7,
                                                          4,
                                                          6,
                                                          6,
                                                          14,
                                                          11,
                                                          3,
                                                          13,
                                                          7,
                                                          11],
                                                 'max': 18,
                                                 'min': 0}]}}
```
