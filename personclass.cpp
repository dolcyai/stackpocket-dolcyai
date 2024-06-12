class Person {
public:
    std::string name;
    int age;

    Person(std::string name, int age) : name(name), age(age) {}

    std::string greet() {
        return "Hello, my name is " + name;
    }
};
