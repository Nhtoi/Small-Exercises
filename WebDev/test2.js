        //!closure

        // function Counter() {
        //     let count = 0;
        //     return {
        //         increment() { count++; },
        //         getCount() { return count; }
        //     };
        // }

        // const c1 = Counter();
        // c1.increment();
        // c1.increment();
        // c1.increment();
        // c1.increment();
        // c1.increment();
        // console.log(c1.getCount()); 

        function addByX(x){
            return function add(num){return console.log(num + x)}
        }
        let initFunc = addByX(2)
        initFunc(2)
        initFunc(3)
        initFunc(4)

        function run (x){
            let result;
            let ran = false
            if (!ran){
                ran = true
                result = initFunc(2)
                return function(args){return result}
            }
        }

        run(addByX(2))
        run(1)
        run(2)
        run(3)
        run(4)

        //function outer(){
            //     let counter = 0
            //     function incrementCounter(){ counter++;}
            //     return incrementCounter;
        
        // }

        // const newFunction = outer();
        // newFunction()
        // newFunction()