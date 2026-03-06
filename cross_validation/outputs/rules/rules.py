def findDecision(obj): #obj[0]: x1, obj[1]: x2, obj[2]: x3, obj[3]: x4
   # {"feature": "x3", "instances": 100, "metric_value": 0.3489, "depth": 1}
   if obj[2]>2.1566798111777374:
      # {"feature": "x4", "instances": 70, "metric_value": 0.0555, "depth": 2}
      if obj[3]<=1.7:
         # {"feature": "x2", "instances": 37, "metric_value": 0.0405, "depth": 3}
         if obj[1]>2.2:
            return 'Iris-versicolor'
         elif obj[1]<=2.2:
            # {"feature": "x1", "instances": 4, "metric_value": 0.3333, "depth": 4}
            if obj[0]>5.0:
               return 'Iris-versicolor'
            elif obj[0]<=5.0:
               return 'Iris-versicolor'
            else:
               return 'Iris-versicolor'
         else:
            return 'Iris-versicolor'
      elif obj[3]>1.7:
         # {"feature": "x1", "instances": 33, "metric_value": 0.0455, "depth": 3}
         if obj[0]>5.9:
            return 'Iris-virginica'
         elif obj[0]<=5.9:
            # {"feature": "x2", "instances": 4, "metric_value": 0.0, "depth": 4}
            if obj[1]<=2.8:
               return 'Iris-virginica'
            elif obj[1]>2.8:
               return 'Iris-versicolor'
            else:
               return 'Iris-virginica'
         else:
            return 'Iris-virginica'
      else:
         return 'Iris-versicolor'
   elif obj[2]<=2.1566798111777374:
      return 'Iris-setosa'
   else:
      return 'Iris-versicolor'
