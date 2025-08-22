class Metro:
    def __init__(self,metro_line,location,destination,amount):
        
        self.metro_line=metro_line
        self.location_in=location
        self.destination_in=destination
        self.amount=amount
        

    def location(self):
        return f'{self.location_in}'
    
    def destination(self):
        return f'{self.destination_in}'
    
    def paid_money(self):
        return f'{self.amount}'
    


class prices(Metro):
    def __init__(self, metro_line, location, destination,amount=0):
        super().__init__(metro_line, location, destination,amount)

    def get_price(self):
            Elmonib_line=['Shubra Elkhima','Mezallat','Khalafawy','St.Treza',
                        'Rod Elfarag','Masarra','Al Shohada','Attaba','Mohamed Najib',   # المحطات ال فخط المنيب
                        'Sadat','Opera','Dokki','El Bohoth','Cairo Universty','Faisal',
                        'Giza','Om Elmasryeen','Sakiat Mekky','El Monib']
            Shubra_Elkhima_line=Elmonib_line[::-1]                                    # المحطات ال فخط شبرا

            Helwan_line= [                                  # المحطات ال فخط حلوان
            "New Marg","El-Marg","Ezbet El-Nakhl","Ain Shams","El-Matareyya","Helmeyet El-Zaitoun",
            "Hadayeq El-Zaitoun","Saray El-Qobba","Hammamat El-Qobba","Kobri El-Qobba","Manshiet El-Sadr",
            "El-Demerdash","Ghamra","Al Shohada","Orabi","Nasser","Sadat","Saad Zaghloul","Al-Sayeda Zeinab",
            "El-Malek El-Saleh","Mar Girgis","El-Zahraa","Dar El-Salam","Hadayeq El-Maadi","Maadi","Sakanat El-Maadi",
            "Tora El-Balad","Kozzika","Tura El-Esmant","Elmasara","Hadayek Helwan","Wadi Hof","Helwan University",
            "Ain Helwan","Helwan"
            ]
            
            Elmarg_line=Helwan_line[::-1]           # المحطات ال فخط المرج

            Rod_El_Farag_Corridor_line = [          # المحطات ال فخط روض الفرح
            "Adly Mansour","Haykestep","Omar Ibn El Khattab","Qobaa","Hesham Barakat","El-Nozha","El-Shams Club",
            "Alf Maskan","Heliopolis","Haroun","Al-Ahram","Koleyet El-Banat","Stadium","Fair Zone","Abbassiya",
            "El-Geish","Bab El-Shaariya","Attaba","Nasser","Maspero","Safaa Hegazy","Kit-Kat",
            "Tawfikia","Wadi El Nile","Gamet El Dowal","Boulak El Dakrour",
            "Imbaba","Sudan","El-Bohy","El-Qawmia","Ring Road","Rod El Farag Corridor"
            ]

            Adly_Mansour_line=Rod_El_Farag_Corridor_line[::-1]          # المحطات ال فخط عدلي منصور

            if self.metro_line== "Elmonib_line":                   # بشيك هو اختار انهي خط
                if self.location_in and self.destination_in in Elmonib_line :
                
                    location_index=Elmonib_line.index(self.location_in)              #مكان المكان ال هو فيه فالليست
                    destination_index=Elmonib_line.index(self.destination_in)        #مكان الوجهه في الليست 
                    count_stations=destination_index-location_index          #بحسب عدد المحطات

                # تحديد السعر
                if count_stations <= 8:
                    return 8
                elif count_stations <= 16:
                    return 10
                elif count_stations <= 23:
                    return 15
                elif count_stations <= 39:
                    return 20
                else:
                    return None
                
            # نفس ال فوق بس علي خط شبرا
            if self.metro_line== "Shubra_Elkhima_line":
                if self.location_in and self.destination_i in Shubra_Elkhima_line :
                
                    location_index=Shubra_Elkhima_line.index(self.location_in)
                    destination_index=Shubra_Elkhima_line.index(self.destination_in)
                    count_stations=destination_index-location_index

                      # تحديد السعر
                    if count_stations <= 8:
                        return 8
                    elif count_stations <= 16:
                        return 10
                    elif count_stations <= 23:
                        return 15
                    elif count_stations <= 39:
                        return 20
                    else:
                        return None
                    

            # خط حلوان
            if self.metro_line== "Helwan_line":                   # بشيك هو اختار انهي خط
                if self.location_in and self.destination_in in Helwan_line :
                
                    location_index=Helwan_line.index(self.location_in)              #مكان المكان ال هو فيه فالليست
                    destination_index=Helwan_line.index(self.destination_in)        #مكان الوجهه في الليست 
                    count_stations=destination_index-location_index          #بحسب عدد المحطات

                # تحديد السعر
                if count_stations <= 8:
                        return 8
                elif count_stations <= 16:
                    return 10
                elif count_stations <= 23:
                    return 15
                elif count_stations <= 39:
                    return 20
                else:
                    return None
                
            
            #خط المرج
            if self.metro_line== "Elmarg_line":                   # بشيك هو اختار انهي خط
                if self.location_in and self.destination_in in Elmarg_line :
                
                    location_index=Elmarg_line.index(self.location_in)              #مكان المكان ال هو فيه فالليست
                    destination_index=Elmarg_line.index(self.destination_in)        #مكان الوجهه في الليست 
                    count_stations=destination_index-location_index          #بحسب عدد المحطات

                # تحديد السعر
                if count_stations <= 8:
                        return 8
                elif count_stations <= 16:
                    return 10
                elif count_stations <= 23:
                    return 15
                elif count_stations <= 39:
                    return 20
                else:
                    return None
            
            # خط كوبري روض الفرج
            if self.metro_line== "Rod_El_Farag_Corridor_line":                   # بشيك هو اختار انهي خط
                if self.location_in and self.destination_in in Rod_El_Farag_Corridor_line :
                
                    location_index=Rod_El_Farag_Corridor_line.index(self.location_in)              #مكان المكان ال هو فيه فالليست
                    destination_index=Rod_El_Farag_Corridor_line.index(self.destination_in)        #مكان الوجهه في الليست 
                    count_stations=destination_index-location_index          #بحسب عدد المحطات

                # تحديد السعر
                if count_stations <= 8:
                        return 8
                elif count_stations <= 16:
                    return 10
                elif count_stations <= 23:
                    return 15
                elif count_stations <= 39:
                    return 20
                else:
                    return None
                
            # خط عدلي منصور
            if self.metro_line== "Adly_Mansour_line":                   # بشيك هو اختار انهي خط
                if self.location_in and self.destination_in in Adly_Mansour_line :
                
                    location_index=Adly_Mansour_line.index(self.location_in)              #مكان المكان ال هو فيه فالليست
                    destination_index=Adly_Mansour_line.index(self.destination_in)        #مكان الوجهه في الليست 
                    count_stations=destination_index-location_index          #بحسب عدد المحطات

                # تحديد السعر
                if count_stations <= 8:
                        return 8
                elif count_stations <= 16:
                    return 10
                elif count_stations <= 23:
                    return 15
                elif count_stations <= 39:
                    return 20
                else:
                    return None



class buy_ticket(prices):                     #  Metro ال وارث من prices كلاس بيورث من ال 
    def __init__(self, metro_line, location, destination, amount):
        super().__init__(metro_line, location, destination, amount)
    
    def buying(self):                               # عمليه الشراء
        real_price=self.get_price()
        if self.amount==8 and real_price==8:
            return f'it\'s your yellow ticket'
            
        elif self.amount>8 and real_price==8:
            return f'it\'s your yellow ticket and {self.amount-8} pounds '
        
        if self.amount==10 and real_price==10:
            return f'it\'s your green ticket'
        elif self.amount>10 and real_price==10:
            return f'it\'s your green ticket and {self.amount-10} pounds'
        
        if self.amount==15 and real_price==15:
            return f'it\'s your pink ticket'
        elif self.amount>15 and real_price==15:
            return f'it\'s your pink ticket and {self.amount-15} pounds'
        
        if self.amount==20 and real_price==20:
            return f'it\'s your lightcafe ticket'
        elif self.amount>20 and real_price==20:
            return f'it\'s your lightcafe and {self.amount-20} pounds'
        else:
            return 'money it\'s not enough'


ask=prices('Elmonib_line','Shubra Elkhima','Dokki')
buying=buy_ticket('Elmonib_line','Shubra Elkhima','Dokki',20)

print("Welcome to Cairo Metro System ")
print('your ticket cost is ',ask.get_price())
print(buying.buying())