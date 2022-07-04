CREATE OR REPLACE table public.employee (
    id INTEGER NOT NULL PRIMARY KEY,
    parent_id INTEGER NULL REFERENCES employee(id) ON DELETE CASCADE,
    "name" TEXT NOT NULL,
    "type" INTEGER check("type" IN (1, 2, 3))
);

CREATE INDEX index_employee_parent_id ON employee(parent_id);