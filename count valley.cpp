for(int i=0;i<steps;i++){
        if (path[i] == 'U' && valley == 0)
            mount++;
        if (path[i] == 'U' && valley > 0)
        {
            valley--;
        if (i != 0 && valley == 0)
            count++;
        }
        if (path[i] == 'D' && mount == 0)
            valley++;
        if (path[i] == 'D' && mount > 0)
            mount--;
}  
return count;
}
