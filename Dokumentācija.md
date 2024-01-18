Šis projekts ir izstrādāts, lai ļautu lietotājam ievadīt atzīmes, saglabāt tās Excel failā un izveidot grafiku ar vidējām atzīmēm. Tas ir noderīgs skolotājiem, lai viegli ievadītu un apstrādātu skolēnu atzīmes.

Projektā tiek izmantotas trīs Python bibliotēkas:

1. pandas: Šī bibliotēka tiek izmantota datu apstrādei un saglabāšanai. Tā ļauj viegli manipulēt ar datiem un saglabāt tos dažādos formātos, tostarp Excel failos.

2. matplotlib.pyplot: Šī bibliotēka tiek izmantota grafiku zīmēšanai. Tā ļauj viegli izveidot dažāda veida grafikus, tostarp stabiņdiagrammas.

3. tkinter: Šī bibliotēka tiek izmantota lietotāja saskarnes izveidei. Tā ļauj viegli izveidot logus, pogas, ievades laukumus un citus widgetus.

Projekta kods sastāv no vairākām daļām:

1. Klase GradeWindow: Šī klase definē logu, kurā lietotājs var ievadīt atzīmes. Tas satur vairākas metodes:
    - __init__: Šī metode inicializē logu un izveido sākotnējos widgetus.
    - create_widgets: Šī metode izveido visus nepieciešamos widgetus, tostarp etiķetes priekšmetiem un darba veidiem, ievades laukumus atzīmēm un pogu atzīmju saglabāšanai.
    - save_grades: Šī metode tiek izsaukta, kad lietotājs nospiež pogu "Saglabāt atzīmes". Tā iegūst atzīmes no ievades laukumiem un saglabā tās vārdnīcā.

2. Funkcijas write_grades_to_excel un plot_average_grades: Šīs funkcijas tiek izmantotas, lai saglabātu atzīmes Excel failā un izveidotu grafiku ar vidējām atzīmēm.

3. Galvenā programma: Galvenā programma izveido GradeWindow instanci, palaista Tkinter notikumu apstrādes ciklu, iegūst atzīmes no GradeWindow, saglabā atzīmes Excel failā un izveido grafiku ar vidējām atzīmēm. 

Lietotājam ir jāpalaiž šis kods, lai parādītu logu, kurā var ievadīt atzīmes. Pēc atzīmju ievadīšanas un saglabāšanas, tās tiek saglabātas Excel failā, un tiek izveidots grafiks ar vidējām atzīmēm. Grafiks tiek saglabāts kā PNG attēls. Atzīmes un grafiks tiek saglabāti norādītajās atrašanās vietās failu sistēmā.
