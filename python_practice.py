
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

results_dic = dict()
for idx in range (0, len(filenames), 1):
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]

    if pet_labels[idx] in classifier_labels[idx]:
        results_dic[filenames[idx]].append(1)
    else:
        results_dic[filenames[idx]].append(0)

for idx in range (0, len(filenames), 1):
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx], 
                                       classifier_label_is_dog[idx]])

for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])                        

    if sum(results_dic[key][2:]) == 3:
        print("*Breed Match*")
    if sum(results_dic[key][3:]) == 2:
        print("*Is-a-Dog Match*")
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("*NOT-a-Dog Match*")
