## Topic 2: Database and Data Models

### 2.1 DBMS Overview
The persistence layer is designed to ensure relational integrity, performance, and transactional consistency.

- **Primary DBMS:** PostgreSQL / SQL Server / SQLite.
- **ORM / Data Access:** Entity Framework Core / Dapper / SQLAlchemy.
- **Migration Strategy:** Code-first migrations managed through version control.

### 2.2 Core Entities and Tables
The foundational database entities are described below:

| Table | Description | Key Indexes |
|---|---|---|
| `Users` | Authentication credentials, user profiles, and roles. | `PK_Users_Id`, `UK_Users_Email` |
| `AuditLogs` | Audit trail of security events and operational updates. | `PK_Audit_Id`, `IX_Audit_CreatedAt` |
| `Configurations` | Dynamic system settings and feature toggles. | `PK_Config_Key` |

### 2.3 Migration History
Record every database migration upon release:
- `20260110_InitialMigration`: Baseline schema creation.
- `20260215_AddAuditLogs`: Audit tracking tables and indexes.
