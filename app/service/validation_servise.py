
import re



class validation_service:
    def contains_only_english(self,input_string):
        pattern = re.compile(r'^[a-zA-Z0-9\s]*$')
        if pattern.match(input_string):
            return True
        else:
            return False
        
    def contains_only_persian(self,input_string):
        persian_pattern = re.compile(r'[\u0600-\u06FF0-9\s]+')
        if persian_pattern.fullmatch(input_string):
            return True
        else:
            return False
        

    def BusinessName(self,lang,dispalyName,persianName):
        disNameIsEng = self.contains_only_english(dispalyName)
        disNameIsPer = self.contains_only_persian(dispalyName)
        perNameIsPer = self.contains_only_persian(persianName)
        if len(dispalyName)<3:
            return {'message':'نام برند کوتاه تر از 3 کارکتر است'},403
        if len(dispalyName)>25:
            return {'message':'نام برند بزرگ تر از 25 کارکتر است'},403
        elif lang=='persian' and disNameIsPer == False:
            return {'message':'کارکتر های نام برند با زبان انتخابی همسان نیست'},403
        elif lang=='english' and disNameIsEng == False:
            return {'message':'کارکتر های نام برند با زبان انتخابی همسان نیست'},403
        elif lang=='english' and len(persianName)<3:
            return {'message':'نام فارسی برند کوتاه تر از 3 کارکتر است'},403
        elif lang=='english' and len(persianName)>25:
            return {'message':'نام فارسی برند بزرگ تر از 25 کارکتر است'},403
        elif lang=='english' and perNameIsPer == False:
            return {'message':'نام فارسی برند درست نیست'},403
        else:
            return True, 200


