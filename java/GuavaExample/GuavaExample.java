import com.google.common.base.*;
import com.google.common.collect.*;
import java.util.*;

import static com.google.common.base.Preconditions.*;
import static com.google.common.collect.Lists.*;

class User
{
    long id;
    String second, third;
    public String login;
    
    public User(long id, String login, String second, String third)
    {
        this.id = id;
        this.login = login;
        this.second = second;
        this.third = third;
    }
    
    public String getFirstName()
    {
        return second;
    }

    public String getLastName()
    {
        return third;
    }
}

public class GuavaExample {
    private class ShouldNotHaveDigitsInLoginPredicate implements Predicate<User>
    {
        @Override
        public boolean apply(User user) {
            checkNotNull(user);
            return CharMatcher.DIGIT.retainFrom(user.login).length() == 0;
        }
    }

    private class FullNameFunction implements Function<User, String>
    {
        @Override
        public String apply(User user) {
            checkNotNull(user);
            return user.getFirstName() + " " + user.getLastName();
        }
    }

    public static void main(String[] args)
    {
        GuavaExample g = new GuavaExample();
        g.run();
    }

    private void run()
    {
        List<User> users = newArrayList(new User(1L, "sylwek", "stall", "rambo"), new User(2L, "arnold", "schwartz", "commando"));
        List<String> fullNames = transform(users, new FullNameFunction());
        
        for (String fullName : fullNames)
        {
            System.out.println(fullName);
        }
        
        /*
        List<User> users = newArrayList(new User(1L, "sylwek", "stall", "rambo"),
          new User(2L, "arnold", "schwartz", "commando"),
          new User(3L, "hans", "kloss", "jw23"));
        Collection<User> usersWithoutDigitsInLogin = filter(users, new ShouldNotHaveDigitsInLoginPredicate());
        String names = Joiner.on("\n").join( transform(usersWithoutDigitsInLogin, new FullNameFunction()) );
        */
    }
}
