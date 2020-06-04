using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public class Moves
    {
        public string name;
        public int priority;
        public MoveTypes category;


        public Moves(string mname, int prio, MoveTypes cat)
        {
            // This constructor will take info from serebii.net, create an object, and store the object information in database

            //TODO: insert data into a database if not already present
        }

        public Moves(string mname)
        {
            // This will be called if the database is already full
            // TODO: find the move in database with mname == name amd set values
        }

    }
}