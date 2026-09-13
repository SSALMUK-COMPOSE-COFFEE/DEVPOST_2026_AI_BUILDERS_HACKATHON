import uuid
from datetime import datetime, timezone

from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from killscore.db import Base


def new_id() -> str:
    return uuid.uuid4().hex[:12]


def now() -> datetime:
    return datetime.now(timezone.utc)


class Org(Base):
    __tablename__ = "org"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    name: Mapped[str] = mapped_column(String)
    plan: Mapped[str] = mapped_column(String, default="free")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)


class User(Base):
    __tablename__ = "user"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    email: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)


class Membership(Base):
    __tablename__ = "membership"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    org_id: Mapped[str] = mapped_column(ForeignKey("org.id"))
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    role: Mapped[str] = mapped_column(String, default="member")


class Repo(Base):
    __tablename__ = "repo"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    org_id: Mapped[str] = mapped_column(ForeignKey("org.id"))
    slug: Mapped[str] = mapped_column(String, unique=True)
    path: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    runs: Mapped[list["Run"]] = relationship(back_populates="repo")


class Run(Base):
    __tablename__ = "run"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    repo_id: Mapped[str | None] = mapped_column(ForeignKey("repo.id"), nullable=True)
    status: Mapped[str] = mapped_column(String, default="queued")
    diff_only: Mapped[bool] = mapped_column(Boolean, default=True)
    base_ref: Mapped[str | None] = mapped_column(String, nullable=True)
    baseline_passed: Mapped[int] = mapped_column(Integer, default=0)
    line_coverage: Mapped[float | None] = mapped_column(Float, nullable=True)
    total: Mapped[int] = mapped_column(Integer, default=0)
    killed: Mapped[int] = mapped_column(Integer, default=0)
    survived: Mapped[int] = mapped_column(Integer, default=0)
    timeout: Mapped[int] = mapped_column(Integer, default=0)
    error: Mapped[int] = mapped_column(Integer, default=0)
    mutation_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    repo: Mapped["Repo | None"] = relationship(back_populates="runs")
    mutants: Mapped[list["Mutant"]] = relationship(back_populates="run", cascade="all, delete-orphan")
    targets: Mapped[list["TargetFunction"]] = relationship(back_populates="run", cascade="all, delete-orphan")


class TargetFunction(Base):
    __tablename__ = "target_function"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    run_id: Mapped[str] = mapped_column(ForeignKey("run.id"))
    file: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    line_start: Mapped[int] = mapped_column(Integer, default=0)
    line_end: Mapped[int] = mapped_column(Integer, default=0)
    run: Mapped["Run"] = relationship(back_populates="targets")


class Mutant(Base):
    __tablename__ = "mutant"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    run_id: Mapped[str] = mapped_column(ForeignKey("run.id"))
    key: Mapped[str] = mapped_column(String)
    file: Mapped[str] = mapped_column(String)
    function: Mapped[str] = mapped_column(String)
    operator: Mapped[str] = mapped_column(String)
    line: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    original_source: Mapped[str] = mapped_column(Text)
    mutant_source: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String, default="pending")
    cluster: Mapped[str | None] = mapped_column(String, nullable=True)
    run: Mapped["Run"] = relationship(back_populates="mutants")
    executions: Mapped[list["TestExecution"]] = relationship(back_populates="mutant", cascade="all, delete-orphan")
    proposals: Mapped[list["ProposedTest"]] = relationship(back_populates="mutant", cascade="all, delete-orphan")


class TestExecution(Base):
    __tablename__ = "test_execution"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    mutant_id: Mapped[str] = mapped_column(ForeignKey("mutant.id"))
    phase: Mapped[str] = mapped_column(String)
    exit_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    duration_ms: Mapped[int] = mapped_column(Integer, default=0)
    stdout_tail: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    mutant: Mapped["Mutant"] = relationship(back_populates="executions")


class ProposedTest(Base):
    __tablename__ = "proposed_test"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    mutant_id: Mapped[str] = mapped_column(ForeignKey("mutant.id"))
    test_name: Mapped[str] = mapped_column(String, default="")
    source: Mapped[str] = mapped_column(Text)
    rationale: Mapped[str] = mapped_column(Text, default="")
    verdict: Mapped[str] = mapped_column(String, default="pending")
    original_exit: Mapped[int | None] = mapped_column(Integer, nullable=True)
    mutant_exit: Mapped[int | None] = mapped_column(Integer, nullable=True)
    llm_call_id: Mapped[str | None] = mapped_column(ForeignKey("llm_call.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    mutant: Mapped["Mutant"] = relationship(back_populates="proposals")


class GatePolicy(Base):
    __tablename__ = "gate_policy"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    repo_id: Mapped[str] = mapped_column(ForeignKey("repo.id"), unique=True)
    min_score: Mapped[float] = mapped_column(Float, default=0.6)
    max_survivors_in_paths: Mapped[int] = mapped_column(Integer, default=0)
    critical_paths: Mapped[list] = mapped_column(JSON, default=list)


class EvidenceExport(Base):
    __tablename__ = "evidence_export"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    run_id: Mapped[str] = mapped_column(ForeignKey("run.id"))
    sha256: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)


class LLMCall(Base):
    __tablename__ = "llm_call"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=new_id)
    run_id: Mapped[str | None] = mapped_column(ForeignKey("run.id"), nullable=True)
    purpose: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    input_tok: Mapped[int] = mapped_column(Integer, default=0)
    output_tok: Mapped[int] = mapped_column(Integer, default=0)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)
    ok: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
