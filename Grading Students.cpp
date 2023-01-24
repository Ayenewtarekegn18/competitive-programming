vector<int> gradingStudents(vector<int> grades)
{
    int n= grades.size();
    for(int i=0;i<n;i++){
        if (grades.at(i)>=38){
           if ((grades.at(i)+2)%5==0)
            grades.at(i)=grades.at(i)+2;
           if ((grades.at(i)+1)%5==0)
            grades.at(i)=grades.at(i)+1;
        } 
        else 
        continue;
    }
    return grades;
}
