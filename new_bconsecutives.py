def b_consecutives ( pattern:list , max_consecutives:int)->list[list]:
    """
    detects if there are consecutive numbers in the pattern
    it could be a consecutive pair 2 times 
    it could be a consecutive pair 1 times
    it could be a 3 consecutive numbers
    it could be 3 consecutive numbers 
    """
    matched:int =0
    consecutive_sequences =[]
    sequence_started_at:int=0
    
    for index ,  item in enumerate(pattern):
        # check if the current item is equal to the next item
        lookforward_index = index+1 if index < len(pattern)-1 else lookforward_index
        print(f" comparing {item} with {pattern[lookforward_index]}")
        if item+1 == pattern[lookforward_index]:
            print(f" comparing {item} with {pattern[lookforward_index]}")
            print(f" the current index is {index}")
            sequence_started_at = index if matched ==0 else sequence_started_at
            matched = matched +1
             
        
            print(f" matched = {matched} before if condition")
            
        else:
            print(f"We have a break in consequent numbers and matched ={matched}")
            print(f" !!!sequence_started_at = {sequence_started_at} and matched ={matched}")
            conseq_items:list = pattern[sequence_started_at:sequence_started_at+matched+1]
            print(f" ---------------> conseq_items={conseq_items}")
            if len(conseq_items) > 1:
                consecutive_sequences.append(conseq_items)
                print(f" current consequtive items is {consecutive_sequences}")
                print(f" conseq_items = {conseq_items}")
                   
            print(f" break when we have sequence of {conseq_items}")
            matched=0
            sequence_started_at=0

    print(f"we have found the following : {consecutive_sequences}")
    
    return  consecutive_sequences




def main():
    mypattern:list[int] = [1,2,3,32,33]
    print(f"the pattern is {mypattern}")
    b_consecutives(mypattern,0)
    
    
    mypattern=[10,13,18,31,39]
    b_consecutives(mypattern,0)

    mypattern=[1,2,20,24,25,28 ,38,39]
    b_consecutives(mypattern,0) 

if __name__ == "__main__":
    main()


