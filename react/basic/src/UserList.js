import React , {useEffect} from "react";

const User = React.memo(function User({user, onRemove, onToggle }) {
    useEffect(() => {
        console.log('user value setted...')
        console.log(user)
        return () => {
            console.log('before user value')
            console.log('user');
        };
    }, [user]);
    return (
        <div>
            <b style={{ cursor: 'pointer', color: user.active ? 'green' : 'black' }}
            onClick={()=> onToggle(user.id)}> {user.username}</b>
            <b>{user.useranme}</b>-<span>{user.email}</span>
            <button onClick= {() => onRemove(user.id)}> 삭제 </button>
        </div>
    );
});

function UserList({ users, onRemove, onToggle }) {
    return (
        <div>
            {users.map(user => (
                    <User user={user} key={user.id} onRemove={onRemove} onToggle={onToggle} />
                // users.map((user, index) => (
                //     <User user={user} key={index} />
                ))
            }
        </div>
    );
}

export default UserList;