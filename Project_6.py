### Polypharmacy side-effect association network

############ Project 6 ############ 
import gzip

filename="/home/ioanna/metaptixiako/kanterakis/ChChSe-Decagon_polypharmacy.csv.gz"

def generate_lines(filename): #generator that gives lines one by one from a gz file
    with gzip.open(filename, 'rt') as f:
        next(f) #we do not want the first line
        for line in f:
            yield line


def find_connections(filename): #returns a dict where the keys are the diseases and the values are dicts. in each dict the keys are the drugs and their values are the drugs that they have a connection with 
    diseases_dict={}
    line_generator=generate_lines(filename)

    for line in line_generator:
        line=line.strip()
        words=line.split(',')
        drug1=words[0]
        drug2=words[1]
        disease_name=words[3].strip()
        if disease_name not in diseases_dict:
            diseases_dict[disease_name]={}
        connections=diseases_dict[disease_name]
        if drug1 not in connections:
            connections[drug1]=set()
        if drug2 not in connections:
            connections[drug2]=set()
        connections[drug1].add(drug2) #each drug is the key in a dict and the values are drugs they have a connection with
        connections[drug2].add(drug1)
    
    return diseases_dict

def find_one_component(start_drug, connections, drugs_left_to_see): #it takes a starting drug, a dict that is the value of a dict of a disease and a set of all the drugs of the disease. it returns a set with all the connections of the starting drug
    component_of_drug=set()
    drugs_we_find=[start_drug] #the order in which we check the drugs for their connections
    drugs_left_to_see.remove(start_drug)

    while drugs_we_find:
        current_drug=drugs_we_find.pop(0)
        component_of_drug.add(current_drug)
        for connection in connections[current_drug]:
            if connection in drugs_left_to_see:
                drugs_we_find.append(connection)
                drugs_left_to_see.remove(connection)

    return component_of_drug


def analyze_connections(disease_dict): #it gets the dict with all the diseases and finds how many components each disease has
    max_component_size=0
    disease_with_biggest_one_component=None
    bonus_results=[]

    for disease_name, connections in disease_dict.items():
        components_sizes=[]
        drugs_left_to_see=set(connections.keys())
        while drugs_left_to_see:
            start_drug=drugs_left_to_see.pop()
            drugs_left_to_see.add(start_drug)
            component=find_one_component(start_drug,connections,drugs_left_to_see)
            components_sizes.append(len(component))
        
        number_of_components=len(components_sizes)

        if number_of_components>0:    
            if number_of_components==1:
                components_size=components_sizes[0]
                if components_size>max_component_size:
                    max_component_size=components_size
                    disease_with_biggest_one_component=disease_name

            
            average_size=sum(components_sizes)/number_of_components
            bonus_results.append((disease_name,number_of_components,average_size))
        
    print("Results")
    print(f'The disease with the largest one component is {disease_with_biggest_one_component} with {max_component_size} nodes/drugs')
    print('Bonus results')
    for name,number,size in bonus_results:
        print(f'The disease {name} has {number} components with an average size of {size}')
        

diseases_dict=find_connections(filename)
print(f'We have {len(diseases_dict)} diseases')
analyze_connections(diseases_dict)