import os
import label_image as li

def main():

  models = ["Resnet","Inception","Mobilenet", "Nasnet", "Pnasnet"]
  res = [224,299,224,331,331]

  #Inception (299*299)
  #Mobilenet (224*224)
  #Nasnet (331*331)
  #Pnasnet (331*331)
  #Resnet (224*224)

  mydir = "G:/My Drive/Analytic Apps/DApps_Project/Test_Images/"

  for j in range(len(models)):
    preds = []
    acts = []
    print(models[j])
    for dirs, subdirs, files in os.walk(mydir):
      for f in  files:
        # Create actual classes
        if 'dnp' in f:
      	  acts.append('dog not pooping')
        else:
      	  acts.append('dog pooping')

        # Build path to test image, model graph, and model label
        if f == "desktop.ini":
          continue
        image = dirs + f
        graph = "G:/My Drive/Analytic Apps/DApps_Project/Models/" +models[j] +"/2/output_graph.pb"
        labels = "G:/My Drive/Analytic Apps/DApps_Project/Models/" +models[j] +"/2/output_labels.txt"
        print(image)
        #print(graph)
        #print(labels)

        # Get the predicted classes
        preds.append(li.label_image(graph=graph, labels=labels, image=image, height=res[j], width=res[j]))

    #print(preds)
    #print(acts)

    # Build the confusion matrix
    cf = [ #Actual
           [0,0],  #Predicted - DP
           [0,0]  #          - DNP
         ]

    correct = 0
    total = len(preds)

    for i in range( len(preds) ):
      if preds[i] == 'dog pooping' and acts[i] == 'dog pooping':
        cf[0][0] += 1

      elif preds[i] == 'dog pooping' and acts[i] == 'dog not pooping':
        cf[0][1] += 1

      elif preds[i] == 'dog not pooping' and acts[i] == 'dog pooping':
        cf[1][0] += 1

      elif preds[i] == 'dog not pooping' and acts[i] == 'dog not pooping':
        cf[1][1] += 1

    print(cf)
    print()

    # Calculate the metrics for the model
    accuracy = (cf[0][0] + cf[1][1]) / total
    recall = cf[0][0] / (cf[0][0] + cf[1][0])
    precision = cf[0][0] / (cf[0][0] + cf[0][1])

    print('Accuracy:', accuracy)
    print('Recall:', recall)
    print('Precision:', precision)

    # Write out results to a text file
    out = open("G:/My Drive/Analytic Apps/DApps_Project/Results/" +models[j] +'3', "w")
    out.write(models[j] +" Results\n")
    out.write("Confusion Matrix\n")
    out.write(str(cf[0][0]) +" " +str(cf[0][1]) +"\n")
    out.write(str(cf[1][0]) +" " +str(cf[1][1]) +"\n")
    out.write("Accuracy\n")
    out.write(str(accuracy) +"\n")
    out.write("Recall\n")
    out.write(str(recall) +"\n")
    out.write("Precision\n")
    out.write(str(precision) +"\n")
    out.close()

main()