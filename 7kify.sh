IN=meow.png
OUT=canvas.png

rm tmp2.png -f
rm tmp.png -f
echo -ne   "[                          ]"
convert $IN -resize 7280x2000 tmp.png
echo -ne "\r[>                         ]"
convert -size 7280x2000 xc:black tmp2.png
convert tmp2.png -draw "image over 0,0 0,0 tmp.png" tmp2.png
echo -ne "\r[=>                        ]"

convert -size 5200x3520 xc:black $OUT
echo -ne "\r[==>                       ]"

# 1
rm tmp.png -f
convert tmp2.png -crop "500x893+0+67" tmp.png
echo -ne "\r[===>                      ]"
convert canvas.png -draw "image over 0,0 768,1360 tmp.png" canvas.png
echo -ne "\r[====>                     ]"

rm tmp.png -f
convert tmp2.png -crop "700x1245+580+71" tmp.png
echo -ne "\r[=====>                    ]"
convert canvas.png -draw "image over 768,0 768,1360 tmp.png" canvas.png
echo -ne "\r[======>                   ]"

rm tmp.png -f
convert tmp2.png -crop "1511x850+1376+466" tmp.png
echo -ne "\r[=======>                  ]"
convert canvas.png -draw "image over 840,1360 1920,1080 tmp.png" canvas.png
echo -ne "\r[========>                 ]"

rm tmp.png -f
convert tmp2.png -crop "893x500+45+1420" tmp.png
echo -ne "\r[=========>                ]"
convert canvas.png -draw "image over 3840,768 1360,768 tmp.png" canvas.png
echo -ne "\r[==========>               ]"

rm tmp.png -f
convert tmp2.png -crop "893x500+1029+1420" tmp.png
echo -ne "\r[===========>              ]"
convert canvas.png -draw "image over 3840,1536 1360,768 tmp.png" canvas.png
echo -ne "\r[============>             ]"

rm tmp.png -f
convert tmp2.png -crop "893x500+2001+1420" tmp.png
echo -ne "\r[=============>            ]"
convert canvas.png -draw "image over 3840,2304 1360,768 tmp.png" canvas.png
echo -ne "\r[==============>           ]"

rm tmp.png -f
convert tmp2.png -crop "1080x1920+2995+0" tmp.png
echo -ne "\r[===============>          ]"
convert canvas.png -draw "image over 2760,1360 1080,1920 tmp.png" canvas.png
echo -ne "\r[================>         ]"

rm tmp.png -f
convert tmp2.png -crop "700x1245+4181+4" tmp.png
echo -ne "\r[=================>        ]"
convert canvas.png -draw "image over 1536,0 768,1360 tmp.png" canvas.png
echo -ne "\r[==================>       ]"

rm tmp.png -f
convert tmp2.png -crop "700x1245+4978+675" tmp.png
echo -ne "\r[===================>      ]"
convert canvas.png -draw "image ove 2304,0 768,1360 tmp.png" canvas.png
echo -ne "\r[====================>     ]"

rm tmp.png -f
convert tmp2.png -crop "500x893+5777+91" tmp.png
echo -ne "\r[=====================>    ]"
convert canvas.png -draw "image over 3072,0 768,1360 tmp.png" canvas.png
echo -ne "\r[======================>   ]"

rm tmp.png -f
convert tmp2.png -crop "893x500+6375+93" tmp.png
echo -ne "\r[=======================>  ]"
convert canvas.png -draw "image over 3840,0 1360,768 tmp.png" canvas.png
echo -ne "\r[========================> ]"

rm tmp.png -f
convert tmp2.png -crop "1511x850+5769+1067" tmp.png
echo -ne "\r[=========================>]"
convert canvas.png -draw "image over 840,2440 1920,1080 tmp.png" canvas.png
echo -e  "\r[==========================]"

rm tmp.png -f
rm tmp2.png -f