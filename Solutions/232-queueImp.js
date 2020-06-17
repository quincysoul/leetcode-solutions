class MyQueue {
    
    constructor()
    {
        this.stack1 = [];
        this.stack2 = [];
        this.s2Front = 0;
        this.front = null;
        this.back = -1;
    }
    
    setQueFront() {
        if(this.stack1.length > 0)
        {
            this.front = this.stack1[this.stack1.length - 1];
        }
        else if(this.stack2.length > 0)
        {
            this.front = this.stack2[this.s2Front] || null;
        }
        else
        {
            this.front = null;
        }
    }

    popQueFront() {

        if(this.stack1.length > 0)
        {
            this.stack1.pop();
            return this.getQueFront()
        }
        else if(this.stack2.length > 0)
        {
            if(this.stack2[this.s2Front])
            {
                let res = this.stack2[this.s2Front];
                this.s2Front++;
                return res;
            }
        }
        else
        {
            return null;
        }
    }
    
    getQueFront() {
        this.setQueFront();
        return this.front;
    }

    push(x) {
            this.stack2.push(x);
    }

    pop() {
        return this.popQueFront();
    }

    peek() {
        return this.getQueFront();
    }

   empty() {

        if(this.getQueFront())
        {
          return false;
        }

        return true;
    }
}
