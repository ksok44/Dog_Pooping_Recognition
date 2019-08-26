import os
import label_image as li
import json

def main():

  models = ["Resnet2","Resnet3","Resnet4","Inception2","Inception3","Inception4",z"Mobilenet2","Mobilenet3","Mobilenet4"]
  res = [224,224,224,299,299,299,224,224,224]

  # Resnet (224 X 224)
  # Inception (299 X 299)
  # Mobilenet (224 X 224)

  mydir = "G:/My Drive/Analytic Apps/DApps_Project/Test_Images/"

  # Read in actuals
  with open("actuals.json", "r") as read_file: # change this line to actuals.json once done testing
    actuals = json.load(read_file)

  actuals = actuals[0]
  # print(actuals)

  # Get a list of all the test images
  images = list(actuals.keys())
  # print(images)

  # Create a dictionary to store predictions for each model
  preds = {}

  # Loop through all the models
  for m in range(len(models)):
    model = models[m][:-1]
    print(model)
    num = models[m][-1:]
    print(num)
    # Loop through all the images
    for dirs, subdirs, files in os.walk(mydir):
      for f in files:
        print(f)
        # Build path to test image, model graph, and model label
        if f == "desktop.ini":
          continue
        image = dirs + f
        graph = "G:/My Drive/Analytic Apps/DApps_Project/Models/" +model +"/" +num +"/output_graph.pb"
        labels = "G:/My Drive/Analytic Apps/DApps_Project/Models/" +model +"/" +num +"/output_labels.txt"
        # print(graph)
        # print(labels)

        # Get the predicted classes
        if models[m] not in preds.keys():
          preds[models[m]] = {}
          preds[ models[m] ][ f ] = li.label_image(graph=graph, labels=labels, image=image, height=res[m], width=res[m])
        else:
           preds[ models[m] ][ f ] = li.label_image(graph=graph, labels=labels, image=image, height=res[m], width=res[m])

  # print(preds)

  # Get the total number of images
  total = len(images)
  # print(total)

  # Create a dictionary to store the accuracy scores for each model tuned on three different learning rates
  acc_obj = {}

  # Loop through each model to create a confusion matrix, accuracy, recall, and precision score and write it out to a file
  for mod in models:

    model = mod[:-1]
    # print(model)

    # Create a 2D list to store the confusion matrix for each model
    cf = [ #Actual
          [0,0],  #Predicted - DP
          [0,0]  #          - DNP
          ]

    # Fill in the confusion matrix
    for img in images:
      if preds[mod][img] == 'dog pooping' and actuals[img] == 'dog pooping':
        cf[0][0] += 1

      elif preds[mod][img] == 'dog pooping' and actuals[img] == 'dog not pooping':
        cf[0][1] += 1

      elif preds[mod][img] == 'dog not pooping' and actuals[img] == 'dog pooping':
        cf[1][0] += 1

      elif preds[mod][img] == 'dog not pooping' and actuals[img] == 'dog not pooping':
        cf[1][1] += 1

    # print(cf)

    # Calculate the metrics for the model based on the confusion matrix
    accuracy = (cf[0][0] + cf[1][1]) / total
    recall = cf[0][0] / (cf[0][0] + cf[1][0])
    precision = cf[0][0] / (cf[0][0] + cf[0][1])

    # print('Accuracy:', accuracy)
    # print('Recall:', recall)
    # print('Precision:', precision)

    # Fill the accuracy dictionary
    if model not in acc_obj.keys():
      acc_obj[model] = [accuracy]
    else:
      acc_obj[model].append(accuracy)

    # Write the confusion matrix and metrics out to a text file
    out = open("G:/My Drive/Analytic Apps/DApps_Project/Results2/" +mod, "w")
    out.write(mod +" Results\n")
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

  # print(acc_obj)

  # Score the ensemble model

  # Create a list that contains the best iteration for model in terms of accuracy
  best_mods = []
  for k,v in acc_obj.items():     
    b_mod = k + str(v.index(max(v))+2)
    best_mods.append(b_mod)

  # print(best_mods)

  ens_preds = {}
  for image in images:
    dp_cnt = 0
    dnp_cnt = 0
    for model in best_mods:
      if preds[model][image] == 'dog pooping':
        dp_cnt += 1
      else:
        dnp_cnt += 1
    if dp_cnt > dnp_cnt:
      ens_preds[image] = 'dog pooping'
    else:
      ens_preds[image] = 'dog not pooping'

  # print(ens_preds)

  # Create a confusion matrix for the ensemble model
  cf_ens = [ #Actual
            [0,0], #Predicted - DP
            [0,0]  #          - DNP
           ]
  
  for im in images:
    if ens_preds[im] == 'dog pooping' and actuals[im] == 'dog pooping':
      cf_ens[0][0] += 1

    elif ens_preds[im] == 'dog pooping' and actuals[im] == 'dog not pooping':
      cf_ens[0][1] += 1

    elif ens_preds[im] == 'dog not pooping' and actuals[im] == 'dog pooping':
      cf_ens[1][0] += 1

    elif ens_preds[im] == 'dog not pooping' and actuals[im] == 'dog not pooping':
      cf_ens[1][1] += 1

  # print(cf_ens)
  # print()

  # Calculate the metrics for the model
  accuracy_ens = (cf_ens[0][0] + cf_ens[1][1]) / total
  recall_ens = cf_ens[0][0] / (cf_ens[0][0] + cf_ens[1][0])
  precision_ens = cf_ens[0][0] / (cf_ens[0][0] + cf_ens[0][1])

  # print('Accuracy:', accuracy_ens)
  # print('Recall:', recall_ens)
  # print('Precision:', precision_ens)

  # Write the confusion matrix and metrics out to a text file
  out = open("G:/My Drive/Analytic Apps/DApps_Project/Results2/Ensemble", "w")
  out.write("Ensemble Results\n")
  out.write("Confusion Matrix\n")
  out.write(str(cf_ens[0][0]) +" " +str(cf_ens[0][1]) +"\n")
  out.write(str(cf_ens[1][0]) +" " +str(cf_ens[1][1]) +"\n")
  out.write("Accuracy\n")
  out.write(str(accuracy_ens) +"\n")
  out.write("Recall\n")
  out.write(str(recall_ens) +"\n")
  out.write("Precision\n")
  out.write(str(precision_ens) +"\n")
  out.close()



main()