temp=0;
preRoot=0;
counter=0;
iterationSize=4;

def degerHesapla(x):

    return (x**3)-(2*x**2)-5;


def kokBul(x1,x2):

    global counter
    global preRoot
    global temp

    val1Key = x1;
    val2Key = x2;
    val1 = degerHesapla(val1Key);
    val2 = degerHesapla(val2Key);

    preRoot=(val1Key + val2Key) / 2;

    if (val1 * val2 < 0):

        print(f"{counter + 1 } .Kök Tahmini : {preRoot}");


        if(degerHesapla(preRoot)>0):

            if(degerHesapla(val1Key)<0):

                temp=val1Key;

            else:

                temp=val2Key;


        else:

            if (degerHesapla(val1Key) > 0):

                temp = val1Key;

            else:

                temp = val2Key;


        counter=counter+1;

        if(counter != iterationSize):

            kokBul(preRoot,temp);



kokBul(2,4);



